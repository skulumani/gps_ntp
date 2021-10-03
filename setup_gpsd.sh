#!/bin/bash

echo "Update GPSD"

GPS_VERSION="3.23.1"
WORK_DIR=$(mktemp -d)

sudo apt-get update
sudo apt purge gpsd

sudo apt-get install -y scons libncurses-dev python-dev python3-dev pps-tools git-core asciidoctor python3-matplotlib build-essential manpages-dev pkg-config

# download GPSD
wget http://download.savannah.gnu.org/releases/gpsd/gpsd-${GPS_VERSION}.tar.gz -O ${WORK_DIR}/gpsd.tar.gz
cd $WORK_DIR

tar -xzf gpsd.tar.gz -C gpsd
cd gpsd

sudo scons
# sudo scons --config=force

sudo scons install

echo "Hold GPSD with apt"
echo "gpsd hold" | sudo dpkg --set-selections
gpsd -V



