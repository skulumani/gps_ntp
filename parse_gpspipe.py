#!/usr/bin/python3

# parse json messages from gpspipe
# documentation here https://gpsd.gitlab.io/gpsd/gpsd_json.html

import sys
import errno
import json
import argparse

# TPV GPSD JSON message
modes = {
    0: 'unknown',
    1: 'nofix',
    2: '2D',
    3: '3D',
}

# these require no extra computations (single value graph)
tpv_targets = {
    'ept': 'Timestamp Error (s)', # seconds
    'epx': 'Longitude Error (m)', # meters
    'epy': 'Latitude Error (m)', # meters
    'epv': 'Altitude Error (m)', # meters
    'lat': 'Latitude (deg)', # degrees
    'lon': 'Longitude (deg)', # degrees
    'alt': 'Altitude (m)', # meters
    'mode': 'Fix Mode', # integer (0, 1, 2, 3)
}

# these do some extra calculations then output a value for MRTG (possibly double value graph)
sky_targets = {
    'sats': 'Satellites',
}

# takes STDIN input from gpspipe -w and parses output into MRTG format based on user defined variable (pick correct key from TPV or SKY messages)

# parse out TPV data for MRTG - will always be a "gauge" graph
# also compute northing/easting error from defined reference
# keys = ['class', 'device', 'mode', 'time', 'ept', 'lat', 'lon', 'alt', 'epx', 'epy', 'epv', 'track', 'speed', 'climb', 'eps', 'epc]

# sys.stdout.write(str(sentence['lat']) + '\n')
# sys.stdout.flush()
def print_custom_targets(sentence, desired_key):
    """Print custom targets for SKY message"""
    
    satellites = sentence['satellites']
    # get total number of satellites
    sats_avail = len(satellites)

    # get satellites used
    sats_used = sum([ s['used'] for s in satellites ])

    print(sats_used)
    print(sats_avail)
    print(0)
    print('Satellites')


if __name__ == "__main__":
    # parse input arguments
    desired_key = sys.argv[1]
    try:
        while True:
            line = sys.stdin.readline()
            if not line:
                break # exit on EOF

            sentence = json.loads(line)
            if sentence['class'] == 'TPV':
                if desired_key in tpv_targets:
                    print(0)
                    print(sentence[desired_key])
                    print(0)
                    print(tpv_targets[desired_key])
                
                    sys.exit(0)
            elif sentence['class'] == 'SKY':
                if desired_key in sky_targets:
                    print_custom_targets(sentence, desired_key)
                    sys.exit(0)


    except IOError as e:
        if e.errno == errno.EPIPE:
            pass
        else:
            raise e

