#!/bin/bash

echo "Install software"

sudo apt-get update

sudo apt-get install gpsd gpsd-clients pps-tools vim tmux git
sudo apt-get install snmpd snmp

# install NTP from source

# add deb source for apt
if grep -q "#deb-src http://raspberrypi.org/raspbian buster main contrib non-free rpi" /etc/apt/sources.list; then
    echo "Deb-src is disabled"
    echo "deb-src http://raspian.raspberrypi.org/raspbian/ buster main contrib non-free rpi" >> /etc/apt/sources.list
else
    echo "Deb-src enabled"
fi

sudo apt-get update
sudo apt-get -y build-dep ntp

echo "Downloading latest ntp"
mkdir -p  /tmp/ntp
wget http://www.eecis.udel.edu/~ntp/ntp_spool/ntp4/ntp-4.2/ntp-4.2.8p15.tar.gz -O /tmp/ntp.tar.gz
tar -xvzf /tmp/ntp.tar.gz -C /tmp/ntp

cd /tmp/ntp
./confgure --prefix=/usr
make
sudo service ntp stop
sudo make install

echo "ntp hold" | sudo dpkg --set-selections
sudo service ntp start

# disable bluetooth
if grep -q "dtoverlay=pi3-disable-bt" /boot/config.txt; then
    echo "Bluetooth already disabled"
else
    echo "Bluetooth not disabled"
    echo "dtoverlay=pi3-disable-bt" >> /boot/config.txt
fi


# enable pps module
if grep -q "pps-gpio" /etc/modules; then
    echo "PPS GPIO already enabled"
else
    echo "Enabling PPS GPIO"
    echo "pps-gpio" >> /etc/modules
fi

# copy config files to appropriate locations
if [ ! -f /etc/default/gpsd ]; then
    echo "Copying GPSD config file"
    cp gpsd /etc/default/
fi

# change permissions
sudo chown root.dialout /dev/pps0
sudo chown root.dialout /dev/ttyAMA0
sudo usermod -a -G dialout pi

# disable NTP in DHCP
if [ ! -f /etc/dhcp/dhclient.conf ]; then
    cp dhclient.conf /etc/dhcp/dhclient.conf
fi

echo "Disabling NTP via DHCP"
rm /etc/dhcp/dhclient-exit-hooks.d/ntp
rm /lib/dhcpd/dhcpd-hooks/50-ntp.conf

if [ ! -f /etc/ntp.conf ]; then
    cp ntp.conf /etc/ntp.conf
fi

# SNMP setup
if [ ! -f /etc/snmp/snmpd.conf ]; then
    cp snmpd.conf /etc/snmp/snmpd.conf
fi

# restart services
sudo systemctl restart snmpd
sudo systemctl restart ntp

# setup directories for webserver
mkdir -p /home/pi/www

echo "NTP log directory"
mkdir -p /home/pi/ntpstats


# setup I2C screen
sudo apt-get install python3-pip
