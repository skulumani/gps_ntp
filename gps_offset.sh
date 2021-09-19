#!/bin/bash

TIMESPAN="60s"

echo "Determine GPS Serial delay"
# check if file exists and delete if so
if [ -f ~/gps_offset.txt ]; then
rm ~/gps_offset.txt
fi

timeout ${TIMESPAN} watch -n 0.5 "ntpq -pn | grep -E '.GPS. +0 +l +1 ' | tee --append ~/gps_offset.txt"

# compute average
awk '{total=total+$9; count=count+1} END {print "Total:"total; print "Count:"count; print "Avg:"total/count}' ~/gps_offset.txt

