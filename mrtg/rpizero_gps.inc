#---------------------------------------------------------------
#	GPS Satellites
#---------------------------------------------------------------

Target[rpizero_gps_sats]: `gpspipe -w | python3 /home/pi/gps_ntp/parse_gpspipe.py sats`
MaxBytes[rpizero_gps_sats]: 100
MaxBytes2[rpizero_gps_sats]: 100
Title[rpizero_gps_sats]: GPS Satellites
Options[rpizero_gps_sats]: integer, gauge, nopercent, growright, unknaszero
#Colours[rpizero_gps_sats]: BLUE#0033FF, RED#FF0000, BLUE#0033FF, RED#FF0000, 
YLegend[rpizero_gps_sats]: Satellites
ShortLegend[rpizero_gps_sats]: Satellites
LegendI[rpizero_gps_sats]: Used
LegendO[rpizero_gps_sats]: Visible
Legend1[rpizero_gps_sats]: Used
Legend2[rpizero_gps_sats]: Visible
PageTop[rpizero_gps_sats]: <H1>GPS Satellites in view and used</H1>

