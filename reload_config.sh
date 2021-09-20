#!/bin/bash

echo "Reloading SNMP, NTP, MRTG, and Apace"

echo "Copying config files"
sudo cp ./mrtg/. /etc/mrtg/
sudo cp mrtg.conf /etc/apache2/sites-available/mrtg.conf

echo "Restart MRTG"
sudo indexmaker /etc/mrtg.cfg > /home/pi/www/mrtg/index.html
sudo /etc/init.d/mrtg restart

sudo a2ensite mrtg

echo "Restart apache2"
sudo systemctl restart apache2

echo "Restart NTP"
sudo systemctl restart ntp

echo "Restart SNMP"
sudo systemctl restart snmp

