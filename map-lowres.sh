#!/bin/sh
for s in *.conj.mir
#This is a low resolution map on purpose
do (  n=${s%%.conj.mir};
   invert vis=$s map=$n.map beam=$n.beam imsize=512 cell=15 robust=1 options=mfs,double;
   clean  map=$n.map beam=$n.beam out=$n.cln mode=any ;
   restor model=$n.cln beam=$n.beam map=$n.map out=$n.rest  mode=clean ;
   fits   in=$n.rest out=$n.fits op=xyout )
done
