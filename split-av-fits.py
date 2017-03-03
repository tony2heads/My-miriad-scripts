# Assumes an ms has name 'm'
# run inside casapy run 'run -i '
tflagdata(vis=m, mode='elevation', lowerlimit=10, upperlimit=90, action='apply')
nn=vishead(vis=m,mode="get",listitems=[],hdkey="field",hdindex="",hdvalue="")
names=nn[0]
listobs(vis=m)
split(vis=m,outputvis="m10.ms",datacolumn="data",width=3)
# now averaged by 3 channels 600->200
for n in names:
    split(vis="m10.ms",field=n,outputvis=n+".ms",datacolumn="data")
    exportuvfits(vis=n+".ms", fitsfile=n+".fits", datacolumn="data")
#the end

