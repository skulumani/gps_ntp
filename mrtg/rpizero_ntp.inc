#-------------------------------------------------------------------------------
# NTP Offset
#-------------------------------------------------------------------------------

Target[rpizero_ntp_offset]: `ntpq -c rv | python3 /home/pi/gps_ntp/parse_ntp.py offset`
MaxBytes[rpizero_ntp_offset]: 100
MaxBytes2[rpizero_ntp_offset]: 200
Unscaled[rpizero_ntp_offset]: dwmy
Title[rpizero_ntp_offset]: NTP Offset
Options[rpizero_ntp_offset]: integer, gauge, nopercent, growright
YLegend[rpizero_ntp_offset]: offset + 100us
ShortLegend[rpizero_ntp_offset]: us
LegendI[rpizero_ntp_offset]: 
LegendO[rpizero_ntp_offset]: offset + 100us:&nbsp;
Legend1[rpizero_ntp_offset]: n/a
Legend2[rpizero_ntp_offset]: time offset in us, with 100ľs added to ensure it's positive
PageTop[rpizero_ntp_offset]: <H2>NTP Offset</H2>


#-------------------------------------------------------------------------------
# NTP Jitter
#-------------------------------------------------------------------------------

Target[rpizero_ntp_jitter]: `ntpq -c rv | python3 /home/pi/gps_ntp/parse_ntp.py jitter`
MaxBytes[rpizero_ntp_jitter]: 1000000000
Title[rpizero_ntp_jitter]: NTP Jitter
Options[rpizero_ntp_jitter]: integer, gauge, nopercent, growright
YLegend[rpizero_ntp_jitter]: jitter
ShortLegend[rpizero_ntp_jitter]:  
kMG[rpizero_ntp_jitter]: ns,us,ms,s,
LegendI[rpizero_ntp_jitter]: clk_jitter:&nbsp;
LegendO[rpizero_ntp_jitter]: sys_jitter:&nbsp;
Legend1[rpizero_ntp_jitter]: clk_jitter
Legend2[rpizero_ntp_jitter]: sys_jitter
PageTop[rpizero_ntp_jitter]: <H2>NTP Jitter</H2>
