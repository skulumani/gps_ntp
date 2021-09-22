#!/bin/bash

echo "Install rrdtool and python3 bindings"

sudo apt-get install librrd-dev rrdtool libpython-dev
sudo apt-get install python3 python3-pip

pip3 install rrdtool
pip3 install matplotlib

