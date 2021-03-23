#!/bin/bash
  
#       COUNT=0
#       LIST_ACTIVE_CLUSTERS=`aws emr list-clusters --terminated|grep Name|cut -d':' -f2|cut -d' '  -f4|cut -d'=' -f2`
#LIST_ACTIVE_CLUSTERS=`aws emr list-clusters --terminated|jq .Clusters|jq '.[]|select((.Name =="DSS cluster id=emr_with_s3 name=emr_with_s3" ) and .NormalizedInstanceHours > 76)'|jq .Id`

EMR_HOURS=72
EMR_CLUSTER_NAME='DSS cluster id=emr_with_s3 name=emr_with_s3'
LIST_ACTIVE_CLUSTERS=`aws emr list-clusters --active|jq .Clusters|jq --arg EMR_CLUSTER_NAME "$EMR_CLUSTER_NAME" --argjson EMR_HOURS "$EMR_HOURS" '.[]|select((.Name ==$EMR_CLUSTER_NAME ) and .NormalizedInstanceHours >= $EMR_HOURS)'|jq -r .Id`

for i in $LIST_ACTIVE_CLUSTERS
do
        echo "terminating $i"
        aws emr terminate-clusters --cluster-ids $i
done
##date -d "$(date -d @1611154782.753) + 1 hour"
#break
