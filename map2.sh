#!/bin/sh
for s in *.mir
do (  n=${s%%.mir};
   invert vis=$n.mir map=$n.map beam=$n.beam imsize=256 cell=30 robust=1 options=mfs,double;
   clean  map=$n.map beam=$n.beam out=$n.cln mode=any ;
   restor model=$n.cln beam=$n.beam map=$n.map out=$n.rest  mode=clean ;
   fits   in=$n.rest out=$n.fits op=xyout )
done
