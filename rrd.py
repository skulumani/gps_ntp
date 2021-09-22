#!/usr/bin/python3

# create the required RRD databases
import rrdtool
import sys
import os

# RPi data
def create_rrd():
    main_path = "/home/pi/rrd"
    if not os.path.isdir(main_path):
        os.makedires(main_path)
      
  # RPi data
  rrdtool.create(
      os.path.join(main_path, "rpi_data.rrd"),
      "--start", "now", 
      "--step", "10", 
      "DS:cpu_usage_percent:GAUGE:20:0:100",
      "DS:mem_usage_percent:GAUGE:20:0:100",
      "DS:disk_usage_percent:GAUGE:20:0:100",
      "DS:cpu_temp:GAUGE:20:-20:100"
     )

def add_rpi_data():
    pass

def add_gps_stats():
    pass

def add_gps_sats():
    pass

def add_ntp_data():
    pass

# GPS data

# GPS satellites

# NTP data
