#!/bin/bash
for im in *.gif
do (
n=${im%%.gif};
/usr/bin/convert $im $n.png;
)
done