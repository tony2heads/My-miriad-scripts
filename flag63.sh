#!/bin/sh
for v in *.mir
#This is because m063 has bad pointing
do (  
uvflag vis=$v select='antennae(10)' flagval=flag;
 )
done
