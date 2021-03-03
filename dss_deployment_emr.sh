#!/bin/bash
#DSS_USER=${1}
#DSS_VERSION=${2}
#FULL PATH ONLY
#DSS_LICENSE=${3}
echo 'pls provide Linux user name to be created for DSS service account: ' 
read DSS_USER
echo 'which DSS version would you like to install (e.g. 9.0.0): '
read DSS_VERSION
echo 'pls provide full path to license file: '
read DSS_LICENSE
DSSKIT="dataiku-dss-$DSS_VERSION"

#get_abs_filename() {
#  # $1 : relative filename
#  echo "$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
#}

## run with root account
sudo -i -- bash -c "echo '++ adding $DSS_USER' \
&& useradd $DSS_USER \
&& echo 'granting sudo' \
&& usermod -aG wheel $DSS_USER \
&& echo '++ setting password as $DSS_USER'\
&& echo '$DSS_USER:$DSS_USER' | chpasswd $DSS_USER"

## run with DSS service account
sudo -i -u $DSS_USER -- bash -c "echo '++ Downloading kit' \
&& curl -OsS -C - 'https://cdn.downloads.dataiku.com/public/studio/$DSS_VERSION/$DSSKIT.tar.gz' \
&& echo '++ Extracting kit' \
&& tar xf '$DSSKIT.tar.gz' \
&& chown -Rh $DSS_USER:$DSS_USER '$DSSKIT'
"

# installing DSS
sudo -i -u $DSS_USER -- bash -c "\
echo '++ Installing dependencies' \
&& echo '$DSS_USER' | sudo -S ~/$DSSKIT/scripts/install/install-deps.sh -yes\
; echo '++ Installing DSS' \
&& echo $HOME
&& mkdir -p dss_home \
&& $DSSKIT/installer.sh -d dss_home/ -p 12000 -l $DSS_LICENSE \
&& echo '++ Running script to start DSS on boot' \
&& echo '$DSS_USER' | sudo -S ~/$DSSKIT/scripts/install/install-boot.sh /home/$DSS_USER/dss_home $DSS_USER \
"

# Spark integrations
sudo -i -u $DSS_USER -- bash -c "\
echo '++ Installing SPARK integration' \
&& /home/$DSS_USER/dss_home/bin/dssadmin install-spark-integration \
"
