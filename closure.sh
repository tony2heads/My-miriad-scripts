#!/bin/sh
for s in *.conj.mir
do (  n=${s%%.conj.mir};
  closure  options=notriple  interval=10 device=$n-clphi.gif/gif vis=$s > $n.log
  closure  options=notriple,amp  interval=10 device=$n-clamp.gif/gif vis=$s >> $n.log
     echo "Done " $n
)
done
