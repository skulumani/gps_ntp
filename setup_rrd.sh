#!/bin/bash

echo "Install rrdtool and python3 bindings"

sudo apt-get install librrd-dev rrdtool -y
sudo apt-get install python3-pip -y

pip3 install rrdtool
pip3 install matplotlib
pip3 install psutil
