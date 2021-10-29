#!/bin/bash

declare -a list_of_users=("bob" "alice" "julia" "alan")

for user_n_pass in "${list_of_users[@]}"
do
#create keytabs
printf "%b" "addent -password -p $user_n_pass@TEST.DATAIKU.COM -k 1 -e RC4-HMAC\n$user_n_pass\nwrite_kt $user_n_pass.keytab\n" | ktutil
#create Kerberos DB entries 
printf "%b" "add_principal -pw $user_n_pass $user_n_pass@TEST.DATAIKU.COM\n" | kadmin.local
#printf "%b" "read_kt $user_n_pass.keytab\nlist" | ktutil
done
