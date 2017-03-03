#!/bin/sh
here=`pwd`
n=`basename $here`
cgdisp type=pixel labtyp=hms,dms options=full,wedge beamtyp=b,l,4 \
in=$n.rest  device=$n.gif/gif  range=-0.02,0.04,lin,1  
# second part varies with source
