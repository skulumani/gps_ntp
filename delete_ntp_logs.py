#!/usr/bin/python3

import os
import glob
import sys

from time import localtime
from time import strftime
from time import time

xx = os.statvfs("/home/pi/ntpstats")
