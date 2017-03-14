#!/bin/sh

rm -Rf *.map *.beam *.cln *.rest *.cln *.fits

dir=`pwd`
n=`basename $dir`

invert vis=*.uv map=$n.map beam=$n.beam imsize=1024 cell=6 robust=1 options=mfs,double;
clean  map=$n.map beam=$n.beam out=$n.cln mode=any 
restor model=$n.cln beam=$n.beam map=$n.map out=$n.rest  mode=clean 
fits   in=$n.rest out=$n.fits op=xyout 
echo "Done"