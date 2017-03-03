# Assumes an ms has name 'm'
# run inside casapy run 'run -i '
listobs(vis=m)
nn=vishead(vis=m,mode="get",listitems=[],hdkey="field",hdindex="",hdvalue="")
names=nn[0]
print "MS: ",m
print "names: ",names
for n in names:
    print "running on:",n
    split(vis=m,field=n,outputvis=n+".ms",datacolumn="data")
    #now have multiple ms
    exportuvfits(vis=n+".ms", fitsfile=n+".fits", datacolumn="data")
    print "FITS file: ", n+".fits"
#the end

