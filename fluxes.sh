#!/bin/bash
for x in *.mir
do uvflux vis=$x stokes=i,q,u,v options=uvpol >> fluxlist
done