#!/bin/bash

# TODO - make these symbolic links instead of copying

echo "Install MRTG"

sudo apt-get update
sudo apt-get install mrtg


echo "Create MRTG web directory"

mkdir -p /home/pi/www/mrtg
sudo mkdir -p /etc/mrtg

echo "Copying MRTG configuration"
sudo cp mrtg.cfg /etc/mrtg/mrtg.cfg

echo "Setup MRTG with apache"
sudo cp mrtg.conf /etc/apache2/sites-available/mrtg.conf

echo "Copying MRTG init.d script"
sudo cp mrtg_init.d /etc/init.d/mrtg

sudo update-rc.d mrtg defaults

sudo indexmaker /etc/mrtg.cfg > /home/pi/www/mrtg/index.html

sudo a2ensite mrtg
sudo systemctl restart apache2

echo "Now starting MRTG"
#sudo env LANG=C /usr/bin/mrtg /etc/mrtg/mrtg.conf
sudo /etc/init.d/mrtg start
