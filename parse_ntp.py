#!/usr/bin/python3

import sys
import errno
import json

max_usec = 100

def get_offset(line):
    """Extract offset and shift/scale"""
    offset = float(line.split("offset=", 1)[-1].split(',')[0]) * 1000  # offset in microsecond
    # convert -max_usec < offstet < max_usec to 0 < offset < 2* max_usec
    offset = int(offset + max_usec) 
    if offset < 0:
        offset = 0
    elif offset > 2*max_usec:
        offset = 2*max_usec 

    print(0)
    print(offset)
    print(0)
    print("NTP Offset")
    sys.exit(0)

def get_jitter(line):
    """Extract jitter and scale/shift"""
    sys_jitter = float(line.split("sys_jitter=", 1)[-1].split(',')[0]) * 1e6 # nanoseconds
    clk_jitter = float(line.split("clk_jitter=", 1)[-1].split(',')[0]) * 1e6 # nanoseconds

    print(int(clk_jitter))
    print(int(sys_jitter))
    print(0)
    print("Jitter")

    sys.exit(0)
    

if __name__ == "__main__":
    desired_key = sys.argv[1]
    
    try:
        lines = sys.stdin.read()
        
        if lines.find(desired_key) > 0:
            if desired_key == "offset":
                get_offset(lines)
            if desired_key == "jitter":
                print(lines)
                get_jitter(lines)

    except IOError as e:
        if e.errno == errno.EPIPE:
            pass
        else:
            raise e
