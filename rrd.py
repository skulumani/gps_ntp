#!/usr/bin/python3

# create the required RRD databases
import rrdtool
import sys
import os
import psutil
import json
import subprocess
from collections import namedtuple
import time
import datetime


# RPi data
def create_rrd():
    main_path = "/home/pi/rrd"
    if not os.path.isdir(main_path):
        os.makedirs(main_path)

    # Rpi, GPS and NTP Stats
    rrdtool.create(
        os.path.join(main_path, "gps_clock_stats.rrd"),
        "--start", "now", 
        "--step", "16s", 
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
        "RRA:AVERAGE:0.5:64s:7d", # 7 days at 30 seconds
        "RRA:AVERAGE:0.5:320s:365d", # 365.25 days at 5 minutes
        "RRA:MAX:0.5:64s:7d",
        "RRA:MAX:0.5:320s:365d",
        "RRA:MIN:0.5:64s:7d",
        "RRA:MIN:0.5:320s:365d")

def get_rpi_data():
    
    rpi_time = time.time()
    # get cpu usage percent
    cpu_percent = psutil.cpu_percent(interval=0.1)
    # mem usage percent
    memory = psutil.virtual_memory()
    mem_percent = memory.percent

    # disk usage percent
    disk = psutil.disk_usage('/')
    disk_percent = disk.percent

    # cpu temp
    process = subprocess.Popen(['vcgencmd', 'measure_temp'], stdout=subprocess.PIPE, universal_newlines=True)
    output, _error = process.communicate()
    cpu_temp = float(output[output.index('=') + 1:output.rindex("'")])
    
    RPi_data = namedtuple("RPi_data", "cpu_percent mem_percent disk_percent cpu_temp time")
    rpi_data = RPi_data(cpu_percent, mem_percent, disk_percent, cpu_temp, rpi_time)

    return rpi_data

def get_gps_stats():
    # SKY
    process = subprocess.run('gpspipe -w -T %s | grep -m 1 SKY', shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
    message = process.stdout
    
    sky = json.loads(message[message.index(':') + 1:])
    sky['time'] = float(message[0:message.index(':')])
    
    # build PRN data
    prn_el = [-1] * 32
    prn_az = [-1] * 32
    prn_ss = [-1] * 32
    prn_used = [-1] * 32
    
    for sat in sky['satellites']:
        prn = sat['PRN'] - 1
        prn_el[prn] = sat['el']
        prn_az[prn] = sat['az']
        prn_ss[prn] = sat['ss']
        prn_used[prn] = int(sat['used']) 

    # TPV
    process = subprocess.run('gpspipe -w -T %s | grep -m 1 TPV', shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
    message = process.stdout
    
    tpv = json.loads(message[message.index(':') + 1:])
    tpv['time'] = float(message[0:message.index(':')])
    
    # build namedtuple for gps data

    return (sky, tpv)

def get_ntp_data():
    ntp_time = time.time()
    process = subprocess.run('ntpq -c rv', shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
    message = process.stdout
    message = message.replace('\n', '')
    message = message.split(',')
    
    offset = float(message[20][message[20].index("=") + 1:])
    frequency = float(message[21][message[21].index("=") + 1:])
    sys_jitter = float(message[22][message[22].index("=") + 1:])
    clk_jitter = float(message[23][message[23].index("=") + 1:])
    clk_wander = float(message[24][message[24].index("=") + 1:])
   
    # now get ntpq -p data  
    process = subprocess.run("ntpq -p | grep '.PPS.'", shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
    message = process.stdout.split()
    
    pps_offset = float(message[8])
    pps_jitter = float(message[9])

    process = subprocess.run("ntpq -p | grep '.GPS.'", shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
    message = process.stdout.split()

    gps_offset = float(message[8])
    gps_jitter = float(message[9])

    NTP_data = namedtuple("NTP_data", "offset frequency sys_jitter clk_jitter clk_wander pps_offset pps_jitter gps_offset gps_jitter time")
    ntp_data = NTP_data(offset, frequency, sys_jitter, clk_jitter, clk_wander,
                        pps_offset, pps_jitter,
                        gps_offset, gps_jitter, ntp_time)
    
    return ntp_data
 
def update_rrd():
    # need to update all DS at the same time
    pass



# NTP data

if __name__ == "__main__":
    #create_rrd()

    # TODO Add argument parsing create RRD, update rrd, graph rrd
    rpi_data = get_rpi_data()

    (sky, tpv) = get_gps_stats()
    print(sky)

    ntp_data = get_ntp_data()    
    print(ntp_data.time)
