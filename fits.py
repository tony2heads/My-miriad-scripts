
names=("1934-638","2326-502","J2329-4730")
for n in names:
    split(vis=m,outputvis=n+".ms",field=n,datacolumn="data")
#
# can put averaging in here
#
for n in names:
    exportuvfits(vis=n+".ms",fitsfile=n+".fits",datacolumn="data",multisource=False)
