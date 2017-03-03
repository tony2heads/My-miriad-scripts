#!/bin/bash
for v in *.uv
do (
	echo $v;
	mfcal vis=$v interval=5,5,5 refant=4 flux=4.9; 
)
done
