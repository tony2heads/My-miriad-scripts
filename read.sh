#!/bin/sh
# converts fits files to miriad format and adds header data for PKS1934-638
for x in *.fits
do (
	ndot=${x%%fits}
	fits in=$x out=${ndot}mir op=uvin
	puthd in=${ndot}mir/systemp value=20.0
	puthd in=${ndot}mir/jyperk value=20.0
)
done
puthd in=PKS1934-638.mir/source value=1934-638
#puthd in=3C48.mir/source value=3C48
#puthd in=3C138.mir/source value=3C138
