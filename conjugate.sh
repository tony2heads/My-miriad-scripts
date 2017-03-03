#!/bin/sh
# Delete old maps
#rm -Rf *.fits *.map *.cln *.rest *.beam
#
#

for v in *.mir
do (
	n=${v%%.mir};
	uvfix vis=$v options=conjugate out=$n.conj.mir;
	echo "Conjugated" $v
	rm -Rf $v
	echo "Deleted original" $v
)
done
#
