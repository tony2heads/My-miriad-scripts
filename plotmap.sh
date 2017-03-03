#!/bin/sh
for s in *.rest
do (   n=${s%%.rest};
	cgdisp device=$n.ps/ps type=contour slev=p,1.4142 \
 levs1=-16,-8,-4,-2,2,4,8,16,32,64 labtyp=hms beamtyp=t,l options=full\
  region='box(10,10,246,246)' in=$s ;
	echo done $n
)
done
