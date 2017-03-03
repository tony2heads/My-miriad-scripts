#!/usr/bin/env python
# Clip level needs to be found beforehand

#  level is min flux density in Jy

import os
import glob



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


# clip level set to 10mJy a reasonable start

for filen in names:
    print filen+'\n'
    runline="imtab mode=nemo clip=0.01 units=abslolute format='(3F13.3)' in="\
             +filen
    x=os.popen(runline)
    ll=x.readlines()
    for line in ll[2:-1]:
        items=line.split()
        rasec=float(items[0])
        decsec=float(items[1])
        flux=float(items[2])
        print("%s %s %5.3f") % (ra(rasec), dec(decsec), flux)
    print "=============="




