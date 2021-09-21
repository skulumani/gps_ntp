

# TODO

MRTG Plots
* [ ] Plot NTP stats with MRTG - create perl/shell scripts to read data
    * Jitter
    * offset
* [ ] Create GPS stats with MRTG - shell scripts to extract data
    * NMEA sentence format http://aprs.gids.nl/nmea/
    * GPS MRTG - https://www.satsignal.eu/raspberry-pi/monitoring.html#gps
    * Sats visible
    * DOP
    * errors 
    * lat,long,alt
    * `gpspipe -r` and search for GPGGA and GPGSA and parse for stats
* [ ] CPU, Mem, wifi load, CPU temperature, storage
    * Use SNMP OIDs or use a shell script directly
* [ ] Copy all config files to this repo
    * NTP conf
    * GPSD conf
    * SNMP conf
    * MRTG conf
    * apache conf
    * website pages
* [ ] Fix reload config script to move other config files
    * snmp
    * dhclient
    * apache default website config
    * gpsd
    * ntp
    * website files
* [ ] Check on updating the leapsecond file (does NTP do it or do I need to do it)
* [ ] Add current time to Index page with offset
* [ ] Once time is working then join NTP pool - will need to do duckdns and port forwarding on router

NTP Best practices - https://tools.ietf.org/id/draft-ietf-ntp-bcp-06.html#rfc.section.4.4
To get ntp stats use `ntpq -c rv` then grep for desired data
