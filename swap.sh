#!/bin/sh
# swaps polarizations

for v in *.mir
do (
	uvswap vis=$v out=tmp.mir options=xyswap
	rm -Rf $v
	uvredo vis=tmp.mir out=${v} options=chi,nopol,nocal,nopass
	rm -Rf tmp.mir
#	ln -s SW${v}  $v
)
done

