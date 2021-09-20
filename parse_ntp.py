#!/usr/bin/python3

import sys
import errno
import json


try:
    while True:
        line = sys.stdin.readline()
        if not line:
            break # exit on EOF

        if line.find('offset') > 0:
            offset = float(line.split("offset=", 1)[-1].split(',')[0]) * 1000  # offset in microsecond
            print(offset)

except IOError as e:
    if e.errno == errno.EPIPE:
        pass
    else:
        raise e

