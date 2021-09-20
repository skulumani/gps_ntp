

# TODO

MRTG Plots
* [ ] Plot NTP stats with MRTG - create perl/shell scripts to read data
    * Jitter
    * offset
* [ ] Create GPS stats with MRTG - shell scripts to extract data
    * Sats visible
    * DOP
* [ ] CPU, Mem, wifi load, CPU temperature, storage
    * Use SNMP OIDs or use a shell script directly


To get ntp stats use `ntpq -c rv` then grep for desired data
