#!/usr/bin/python3

import os
import glob
import sys

from time import localtime
from time import strftime
from time import time

def get_folder_size(folder):
    "Recursive size of folder in bytes"
    total_size = os.path.getsize(folder)
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += get_folder_size(itempath)

    return total_size

timestr = strftime("%Y-%m-%d %T", localtime())


# define max log directory size
log_directory = "/home/pi/ntpstats"
log_size = get_folder_size(log_directory)
max_size = 10.0 * 1024 * 1024

percent_avail = (max_size - log_size) / max_size * 100

print("{} NTP Logs: {:6.3f}% ({:6.3f} GB) free".format(timestr, percent_avail, (max_size - log_size)/1024/1024), end='')

if percent_avail > 20:
    print()
    sys.exit()

# if greater delete oldest week of files
# find list of files
# sort by oldest

