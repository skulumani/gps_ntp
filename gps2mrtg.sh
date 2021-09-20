#!/bin/bash

# gpspipe -w | grep 'TPV' for position
# gpspipe -w | grep 'SKY' for satellites in view
# https://gpsd.gitlab.io/gpsd/gpsd_json.html for parsing

# number of satellites used in current fix
sats_fix=$(gpspipe -r | awk -W interactive '-F,' '/GPGGA/{print $8;exit}')
echo $sats_fix

# get total satellites in view

# get error

# get lat, long, alt
gpspipe -r | awk -W interactive '-F,' '/GPGSA/
{
    AVAILABLE = -1;
    if ( $1 ~ /GPGSA/ ) {
        for (i=1; i <= NF; i++) {
        
        }
    }

