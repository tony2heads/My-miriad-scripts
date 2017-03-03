#!/bin/sh
for v in *.mir
do (   n=${v%%.conj.mir};
      smauvplt device=${n}_uvdist.gif/gif options=nobase axis=uvdist,amp vis=$v)
done
