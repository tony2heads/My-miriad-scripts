#!/usr/bin/env python
# Clip level needs to be found beforehand

#  level is min flux density in Jy

import mirpy
import glob

level=0.020 # 20mJy

def ra(rasec):
    hh=rasec/(3600*15) # to hours
    hour=int(hh)
    mm=(hh-hour)*60
    minutes=int(mm)
    seconds=60*(mm-minutes)
    hms=("%02d:%02d:%05.2f") %(hour,minutes,seconds)
    return hms

def dec(decsec):
    dd=decsec/3600 # to degrees
    ddabs=abs(dd)
    sign=dd/ddabs
    # NOTE SIGN is +1 or -1
    deg=int(ddabs)
    mm=(ddabs-deg)*60
    minutes=int(mm)
    seconds=60*(mm-minutes)
    dms=("%3d:%02d:%05.2f") %(sign*deg,minutes,seconds)
    if ddabs<1 and sign == -1 :  # for the case close of 0hrs
        dms=(" -0:%02d:%05.2f") %(minutes,seconds)
    return dms



names=sorted(glob.iglob("*.cln")) # gives a sorted list of filenames

for filen in names:
    print filen
    x= mirpy.miriad.imstore(_in=filen, mode="nemo", units="absolute",clip=level)
    ll=x.splitlines()
    # first two lines are listing and last is "Found"
    for line in ll[2:-1]:
        items=line.split()
        rasec=float(items[0])
        decsec=float(items[1])
        flux=float(items[2])
        print("%s %s %5.3f") % (ra(rasec), dec(decsec), flux)
    print "=============="




