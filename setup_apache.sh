#!/bin/bash

# install updates
sudo apt-get update
sudo apt-get upgrade

sudo apt install apache2 -y
sudo apt install php7.3 libapache2-mod-php7.3 php7.3-mbstring -y

echo "Changing user permissions"
sudo usermod -a -G www-data pi
sudo chown -R -f www-data:www-data /var/www/html

echo "Set up webpage"
mkdir -p /home/pi/www/

sudo cp gps_website.conf /etc/apache2/sites-available/000-default.conf
sudo systemctl reload apache2
