#!/bin/bash

TIMESPAN="60s"

echo "Determine GPS Serial delay"
# check if file exists and delete if so
if [ -f ~/gps_offset.txt ]; then
    echo "Removing old log file"
    rm ~/gps_offset.txt
fi
echo "Make sure ntp.conf GPS server has no time offset"
echo "Recording GPS offset"
timeout ${TIMESPAN} watch -n 0.5 "ntpq -pn | grep -E '.GPS. +0 +l +1 ' | tee --append ~/gps_offset.txt"

echo "Finished. Computing average"

# compute average
awk '{total=total+$9; count=count+1} END {print "Total:"total; print "Count:"count; print "Avg:"total/count}' ~/gps_offset.txt

