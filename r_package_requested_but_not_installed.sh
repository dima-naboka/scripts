#!/bin/bash
if [ $# -eq 0 ]; then
	echo "please provide full path to backend.log or apimain.log"
	exit 1
fi

diff <(grep '\* installing \*source\* package' $1 |awk '{print $10}'|gsed "s/[‘’]//g"|sort) <(grep '\* DONE' $1 | awk '{print $8}'|sed -e "s/[()]//g"|sort)
