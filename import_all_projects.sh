#!/bin/bash
#PRJ_DIR=exported_projects
if [ -z "$1" ]
  then
    echo "please specify folder containing projects ZIP files"
fi
exit 1

PRJ_DIR=${1}

#FULL_PATH="$(pwd)/$PRJ_DIR"
##

#mkdir $PRJ_DIR
#echo "$FULL_PATH created"

for i in $(ls $PRJ_DIR)
do
echo "importing $i"
#./bin/dsscli project-import $i 
done
