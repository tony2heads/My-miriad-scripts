#!/bin/bash
dir=`pwd`
n=`basename $dir`
smauvplt device=${n}_amp.gif/gif options=nobase  vis=p*.uv; 
smauvplt device=${n}_uvdist.gif/gif options=nobase axis=uvdist,amp vis=p*.uv;
