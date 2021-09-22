

# TODO
* [ ] `rrdtool`
    * [ ] install rrdtool and python 3 version
    * [ ] Create database
    * [ ] Python script to read data to store (pipe into python then write to rrd)
        * RPI Stats - 1 sec - CPU usage %, Mem usage %, Disk %, CPU temp
        * GPS Stats - 10 sec - lat, lon, alt, epx, epy, epv, xdop, ydop, vdop, tdop, hdop, gdop, pdop
        * GPS Sats - 10 sec - PRN 1-32 each with el, az, ss, used (0 or 1)
        * NTP stats - 16 sec - ntpq -c rv, offset, frequency, sys_jitter, clk_jitter, clk_wander
            * ntpq -p - PPS and GPS each offset and jitter
    * [ ] rrdgraph for simple/recurrent graphs
    * [ ] python export for more complicated plots
* [ ] Python plot for NTP log files
* [ ] Disable MRTG and instead use cron and rrdtool for plots
* [x] Plot NTP stats with MRTG - create perl/shell scripts to read data
    * Jitter
    * offset
* [x] Create GPS stats with MRTG - shell scripts to extract data
    * NMEA sentence format http://aprs.gids.nl/nmea/
    * GPS MRTG - https://www.satsignal.eu/raspberry-pi/monitoring.html#gps
    * Sats visible
    * DOP
    * errors 
    * lat,long,alt
    * `gpspipe -r` and search for GPGGA and GPGSA and parse for stats
* [x] CPU, Mem, wifi load, CPU temperature, storage
    * Use SNMP OIDs or use a shell script directly
* [x] Copy all config files to this repo
    * NTP conf
    * GPSD conf
    * SNMP conf
    * MRTG conf
    * apache conf
    * website pages
* [x] Fix reload config script to move other config files
    * snmp
    * dhclient
    * apache default website config
    * gpsd
    * ntp
    * website files
* [ ] Check on updating the leapsecond file (does NTP do it or do I need to do it)
* [ ] Add current time to Index page with offset using php
* [ ] Once time is working then join NTP pool - will need to do duckdns and port forwarding on router

NTP Best practices - https://tools.ietf.org/id/draft-ietf-ntp-bcp-06.html#rfc.section.4.4
To get ntp stats use `ntpq -c rv` then grep for desired data
