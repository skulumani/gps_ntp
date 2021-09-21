#!/bin/bash

echo "Reloading SNMP, NTP, MRTG, and Apace"

echo "Copying config files"
sudo cp -a ./mrtg/. /etc/mrtg/
sudo cp mrtg.conf /etc/apache2/sites-available/mrtg.conf

sudo cp dhclient.conf /etc/dhcp/dhclient.conf
sudo cp ntp.conf /etc/ntp.conf
sudo cp snmpd.conf /etc/snmp/snmpd.conf

echo "Restart MRTG"
sudo indexmaker --section=title /etc/mrtg/mrtg.cfg > /home/pi/www/mrtg/index.html
sudo /etc/init.d/mrtg restart

sudo a2ensite mrtg

echo "Restart apache2"
sudo systemctl restart apache2

echo "Restart NTP"
sudo systemctl restart ntp

echo "Restart SNMP"
sudo systemctl restart snmpd

