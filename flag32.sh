#!/bin/sh
for v in *.mir
#This is because m032 was bad  has bad pointing
do (  
uvflag vis=$v select='antennae(10) time(16SEP24:11:50:00,16SEP24:13:00:00)' flagval=flag;
 )
done
