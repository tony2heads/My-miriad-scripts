#!/bin/bash
GLOBIGNORE="PKS1934-638.conj.mir"
for v in *.mir
do (
	echo $v
	gpcopy vis=PKS1934-638.conj.mir out=$v ;
	uvflux vis=$v stokes=i options=nopol >> fluxlist.txt ;
)
done
