#!/bin/bash
PRJ_DIR=exported_projects
FULL_PATH="$(PWD)/$PRJ_DIR"

mkdir $PRJ_DIR
echo "$FULL_PATH created"

for i in $(./bin/dsscli projects-list --no-header|cut -d" " -f 1)
do
echo "exporting $i to $FULL_PATH"
#./bin/dsscli project-export $i $PRJ_DIR/$i.zip
done
