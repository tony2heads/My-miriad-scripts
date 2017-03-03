#!/usr/bin/env python
import katdal
import sys
#
filename=sys.argv[1]
#
h5=katdal.open(filename,refant='m001')
for ant in h5.ants:
    ecef=ant.position_ecef
    wgs =ant.ref_position_wgs84
    enu =ant.position_enu
    name =ant.name
    #print "ECEF values", ecef
    #print "WGS84 values",wgs
    print "%s" %(name),
    print "ENU values %6.3f, %6.3f, %6.3f" %( enu)
    #print ant
