#!/bin/sh
for m in *.rest
do cgdisp device=$m.png/png  labtyp=hms,dms beamtyp=t,r options=wedge in=$m
done