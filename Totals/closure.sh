#bin/sh
dir=`pwd`
n=`basename $dir`
closure options=notriple,amp device=${n}_clamp.gif/gif vis=*.uv
closure options=notriple device=${n}_clpha.gif/gif vis=*.uv
