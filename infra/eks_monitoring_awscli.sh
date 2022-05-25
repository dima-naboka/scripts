#!/bin/bash
## This script is designed to save money by terminating EKS cluster and 2 associated CloudFormation stacks (CloudStack implementation) according to "limit" hours variable
## Designed by dmytro.naboka@dataiku.com for TSE subscription 

#when executed manually, log in with "aws sso login --profile dataiku-tse" and uncomment line below when using non-default profile; otherwise requires access key in ~/.aws/credentials 
export AWS_PROFILE="dataiku-tse"
export AWS_DEFAULT_OUTPUT="text"

LIMIT_HOUR=

usage() {
        prog=$(basename "$0")
        echo >&2 "
*** Usage:

  -l : running EKS hours limit
  -p : assigned AWS profile to monitor EKS uptime
  -h : prints this help
  "
        exit 1
}

while getopts l:p:h OPT; do
	case "$OPT" in
	l)
		LIMIT_HOUR="$OPTARG"
		;;
	p)
		AWS_PROFILE="$OPTARG"
		;;
	h)
		usage
		;;
	*)
		usage
		;;
	esac
done

if [ $OPTIND -le $# ]; then
        echo >&2 "[-] Bad usage: invalid argument : ${!OPTIND}"
        usage
fi

#
# Check arguments
#

if [ -z "$LIMIT_HOUR" ]; then
        echo >&2 "[-] Bad usage: LIMIT_HOUR (-l) can't be empty"
	usage
fi

# actual code: loop thru all regions and delete CF stacks for nodegroup, cluster
for region in `aws ec2 describe-regions --query "Regions[].{Name:RegionName}"`; 
do 
  echo "[+] checking $region resources" && \
  for cl_name in `aws eks list-clusters --region=$region --query "clusters"`; 
    do 
       echo -n "[+] $region $cl_name createdAt: " && \
       echo `aws eks describe-cluster --name=$cl_name --region=$region --query "cluster.createdAt"` && \

       #cluster ISO 8601 creation time
       cl_time=`aws eks describe-cluster --name=$cl_name --region=$region --query "cluster.createdAt"` && \

       if [[ $(date -d "$cl_time +$LIMIT_HOUR hours" +"%s") < $(date +"%s") ]] 
       then 
	 echo "[!] $cl_name exceeds $LIMIT_HOUR hour limit; deleting CF stacks" && \

	 #delete *-nodegroup CF
	 for st_name in `aws cloudformation list-stacks --region=$region --query "StackSummaries[?StackStatus=='CREATE_COMPLETE']|[?contains(StackName,'eksctl-$cl_name-nodegroup')].StackName"`;
	 do 
	   stack_id=`aws cloudformation list-stacks --region=$region --query="StackSummaries[?StackStatus=='CREATE_COMPLETE']|[?contains(StackName,'eksctl-$cl_name-nodegroup')].StackId"` && \
	   aws cloudformation delete-stack --region=$region --stack-name $st_name && \

 	   echo "[!] deleting $st_name stack_id:$stack_id" && \
	   while [[ `aws cloudformation list-stacks --region=$region --query "StackSummaries[?StackId=='$stack_id'].StackStatus"` != "DELETE_COMPLETE" ]];
	   do 
	     echo -n "." && \
	     sleep 10 && \
	     if [[ `aws cloudformation list-stacks --region=$region --query "StackSummaries[?StackId=='$stack_id'].StackStatus"` == "DELETE_COMPLETE" ]]; then break; fi
	   done
	 echo "[!] $cl_name-nodegroup deleted"; 
	 done

	 #delete *-cluster CF
	 for st_name in `aws cloudformation list-stacks --region=$region --query "StackSummaries[?StackStatus=='CREATE_COMPLETE']|[?StackName=='eksctl-$cl_name-cluster'].StackName"`;
	 do 
	   stack_id=`aws cloudformation list-stacks --region=$region --query="StackSummaries[?StackStatus=='CREATE_COMPLETE']|[?StackName=='eksctl-$cl_name-cluster'].StackId"` && \
	   aws cloudformation delete-stack --region=$region --stack-name $st_name && \

 	   echo "[!] deleting $st_name stack_id:$stack_id" && \
	   while [[ `aws cloudformation list-stacks --region=$region --query "StackSummaries[?StackId=='$stack_id'].StackStatus"` != "DELETE_COMPLETE" ]];
	   do 
	     echo -n "." && \
	     sleep 10 && \
	     if [[ `aws cloudformation list-stacks --region=$region --query "StackSummaries[?StackId=='$stack_id'].StackStatus"` == "DELETE_COMPLETE" ]]; then break; fi
	   done
	 echo "[!] $cl_name-cluster deleted"; 
	 done

       else 
         echo "[+] $cl_name doesn't exceed $LIMIT_HOUR hour limit"
       fi

  done;
done
