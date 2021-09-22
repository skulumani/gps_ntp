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

    # Rpi, GPS and NTP Stats
    rrdtool.create(
        os.path.join(main_path, "gps_clock_stats.rrd"),
        "--start", "now", 
        "--step", "10", 
        "DS:cpu_usage_percent:GAUGE:32:0:100",
        "DS:mem_usage_percent:GAUGE:32:0:100",
        "DS:disk_usage_percent:GAUGE:32:0:100",
        "DS:cpu_temp:GAUGE:32:-20:100",
        "DS:lat:GAUGE:32:0:90",
        "DS:lon:GAUGE:32:0:180",
        "DS:alt:GAUGE:32:-1000:1000",
        "DS:epx:GAUGE:32:0:U",
        "DS:epy:GAUGE:32:0:U",
        "DS:epv:GAUGE:32:0:U",
        "DS:xdop:GAUGE:32:0:U",
        "DS:ydop:GAUGE:32:0:U",
        "DS:vdop:GAUGE:32:0:U",
        "DS:tdop:GAUGE:32:0:U",
        "DS:hdop:GAUGE:32:0:U",
        "DS:gdop:GAUGE:32:0:U",
        "DS:pdop:GAUGE:32:0:U",
        "DS:PRN1_el:GAUGE:32:0:90",
        "DS:PRN1_az:GAUGE:32:0:360",
        "DS:PRN1_ss:GAUGE:32:0:U",
        "DS:PRN1_used:GAUGE:32:0:1",
        "DS:PRN2_el:GAUGE:32:0:90",
        "DS:PRN2_az:GAUGE:32:0:360",
        "DS:PRN2_ss:GAUGE:32:0:U",
        "DS:PRN2_used:GAUGE:32:0:1",
        "DS:PRN3_el:GAUGE:32:0:90",
        "DS:PRN3_az:GAUGE:32:0:360",
        "DS:PRN3_ss:GAUGE:32:0:U",
        "DS:PRN3_used:GAUGE:32:0:1",
        "DS:PRN4_el:GAUGE:32:0:90",
        "DS:PRN4_az:GAUGE:32:0:360",
        "DS:PRN4_ss:GAUGE:32:0:U",
        "DS:PRN4_used:GAUGE:32:0:1",
        "DS:PRN5_el:GAUGE:32:0:90",
        "DS:PRN5_az:GAUGE:32:0:360",
        "DS:PRN5_ss:GAUGE:32:0:U",
        "DS:PRN5_used:GAUGE:32:0:1",
        "DS:PRN6_el:GAUGE:32:0:90",
        "DS:PRN6_az:GAUGE:32:0:360",
        "DS:PRN6_ss:GAUGE:32:0:U",
        "DS:PRN6_used:GAUGE:32:0:1",
        "DS:PRN7_el:GAUGE:32:0:90",
        "DS:PRN7_az:GAUGE:32:0:360",
        "DS:PRN7_ss:GAUGE:32:0:U",
        "DS:PRN7_used:GAUGE:32:0:1",
        "DS:PRN8_el:GAUGE:32:0:90",
        "DS:PRN8_az:GAUGE:32:0:360",
        "DS:PRN8_ss:GAUGE:32:0:U",
        "DS:PRN8_used:GAUGE:32:0:1",
        "DS:PRN9_el:GAUGE:32:0:90",
        "DS:PRN9_az:GAUGE:32:0:360",
        "DS:PRN9_ss:GAUGE:32:0:U",
        "DS:PRN9_used:GAUGE:32:0:1",
        "DS:PRN10_el:GAUGE:32:0:90",
        "DS:PRN10_az:GAUGE:32:0:360",
        "DS:PRN10_ss:GAUGE:32:0:U",
        "DS:PRN10_used:GAUGE:32:0:1",
        "DS:PRN11_el:GAUGE:32:0:90",
        "DS:PRN11_az:GAUGE:32:0:360",
        "DS:PRN11_ss:GAUGE:32:0:U",
        "DS:PRN11_used:GAUGE:32:0:1",
        "DS:PRN12_el:GAUGE:32:0:90",
        "DS:PRN12_az:GAUGE:32:0:360",
        "DS:PRN12_ss:GAUGE:32:0:U",
        "DS:PRN12_used:GAUGE:32:0:1",
        "DS:PRN13_el:GAUGE:32:0:90",
        "DS:PRN13_az:GAUGE:32:0:360",
        "DS:PRN13_ss:GAUGE:32:0:U",
        "DS:PRN13_used:GAUGE:32:0:1",
        "DS:PRN14_el:GAUGE:32:0:90",
        "DS:PRN14_az:GAUGE:32:0:360",
        "DS:PRN14_ss:GAUGE:32:0:U",
        "DS:PRN14_used:GAUGE:32:0:1",
        "DS:PRN15_el:GAUGE:32:0:90",
        "DS:PRN15_az:GAUGE:32:0:360",
        "DS:PRN15_ss:GAUGE:32:0:U",
        "DS:PRN15_used:GAUGE:32:0:1",
        "DS:PRN16_el:GAUGE:32:0:90",
        "DS:PRN16_az:GAUGE:32:0:360",
        "DS:PRN16_ss:GAUGE:32:0:U",
        "DS:PRN16_used:GAUGE:32:0:1",
        "DS:PRN17_el:GAUGE:32:0:90",
        "DS:PRN17_az:GAUGE:32:0:360",
        "DS:PRN17_ss:GAUGE:32:0:U",
        "DS:PRN17_used:GAUGE:32:0:1",
        "DS:PRN18_el:GAUGE:32:0:90",
        "DS:PRN18_az:GAUGE:32:0:360",
        "DS:PRN18_ss:GAUGE:32:0:U",
        "DS:PRN18_used:GAUGE:32:0:1",
        "DS:PRN19_el:GAUGE:32:0:90",
        "DS:PRN19_az:GAUGE:32:0:360",
        "DS:PRN19_ss:GAUGE:32:0:U",
        "DS:PRN19_used:GAUGE:32:0:1",
        "DS:PRN20_el:GAUGE:32:0:90",
        "DS:PRN20_az:GAUGE:32:0:360",
        "DS:PRN20_ss:GAUGE:32:0:U",
        "DS:PRN20_used:GAUGE:32:0:1",
        "DS:PRN21_el:GAUGE:32:0:90",
        "DS:PRN21_az:GAUGE:32:0:360",
        "DS:PRN21_ss:GAUGE:32:0:U",
        "DS:PRN21_used:GAUGE:32:0:1",
        "DS:PRN22_el:GAUGE:32:0:90",
        "DS:PRN22_az:GAUGE:32:0:360",
        "DS:PRN22_ss:GAUGE:32:0:U",
        "DS:PRN22_used:GAUGE:32:0:1",
        "DS:PRN23_el:GAUGE:32:0:90",
        "DS:PRN23_az:GAUGE:32:0:360",
        "DS:PRN23_ss:GAUGE:32:0:U",
        "DS:PRN23_used:GAUGE:32:0:1",
        "DS:PRN24_el:GAUGE:32:0:90",
        "DS:PRN24_az:GAUGE:32:0:360",
        "DS:PRN24_ss:GAUGE:32:0:U",
        "DS:PRN24_used:GAUGE:32:0:1",
        "DS:PRN25_el:GAUGE:32:0:90",
        "DS:PRN25_az:GAUGE:32:0:360",
        "DS:PRN25_ss:GAUGE:32:0:U",
        "DS:PRN25_used:GAUGE:32:0:1",
        "DS:PRN26_el:GAUGE:32:0:90",
        "DS:PRN26_az:GAUGE:32:0:360",
        "DS:PRN26_ss:GAUGE:32:0:U",
        "DS:PRN26_used:GAUGE:32:0:1",
        "DS:PRN27_el:GAUGE:32:0:90",
        "DS:PRN27_az:GAUGE:32:0:360",
        "DS:PRN27_ss:GAUGE:32:0:U",
        "DS:PRN27_used:GAUGE:32:0:1",
        "DS:PRN28_el:GAUGE:32:0:90",
        "DS:PRN28_az:GAUGE:32:0:360",
        "DS:PRN28_ss:GAUGE:32:0:U",
        "DS:PRN28_used:GAUGE:32:0:1",
        "DS:PRN29_el:GAUGE:32:0:90",
        "DS:PRN29_az:GAUGE:32:0:360",
        "DS:PRN29_ss:GAUGE:32:0:U",
        "DS:PRN29_used:GAUGE:32:0:1",
        "DS:PRN30_el:GAUGE:32:0:90",
        "DS:PRN30_az:GAUGE:32:0:360",
        "DS:PRN30_ss:GAUGE:32:0:U",
        "DS:PRN30_used:GAUGE:32:0:1",
        "DS:PRN31_el:GAUGE:32:0:90",
        "DS:PRN31_az:GAUGE:32:0:360",
        "DS:PRN31_ss:GAUGE:32:0:U",
        "DS:PRN31_used:GAUGE:32:0:1",
        "DS:PRN32_el:GAUGE:32:0:90",
        "DS:PRN32_az:GAUGE:32:0:360",
        "DS:PRN32_ss:GAUGE:32:0:U",
        "DS:PRN32_used:GAUGE:32:0:1",
        "DS:ntp_offset:GAUGE:32:-10:10", # units in ms
        "DS:ntp_frequency:GAUGE:32:-100:100", # units in ppm
        "DS:ntp_sys_jitter:GAUGE:32:0:100", # units in ms
        "DS:ntp_clk_jitter:GAUGE:32:0:100", # units in ms
        "DS:ntp_clk_wander:GAUGE:32:0:100", # units in ppm
        "DS:ntp_pps_offset:GAUGE:32:-100:100", # units in ms
        "DS:ntp_pps_jitter:GAUGE:32:0:100", # units in ms
        "DS:ntp_gps_offset:GAUGE:32:-100:100", # units in ms
        "DS:ntp_gps_jitter:GAUGE:32:0:100", # units in ms
        "RRA:AVERAGE:0.5:1.875:20160", # 7 days at 30 seconds
        "RRA:AVERAGE:0.5:18.75:105192", # 365.25 days at 5 minutes
        "RRA:MAX:0.5:1.875:20160", 
        "RRA:MAX:0.5:18.75:105192",
        "RRA:MIN:0.5:1.875:20160",
        "RRA:MIN:0.5:18.75:105192",
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
