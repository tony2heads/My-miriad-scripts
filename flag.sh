
#!/bin/bash
for v in *.mir
do (
    uvflag vis=$v line=channel,15,228 flagval=flag;
    uvflag vis=$v line=channel,15,488 flagval=flag;
    uvflag vis=$v line=channel,994,502 flagval=flag;
    uvflag vis=$v line=channel,48,1495  flagval=flag;
    uvflag vis=$v line=channel,1,2102 flagval=flag;
    uvflag vis=$v line=channel,60,2322 flagval=flag;
    uvflag vis=$v line=channel,5,2382 flagval=flag;
    uvflag vis=$v line=channel,12,2431 flagval=flag;
    uvflag vis=$v line=channel,4,2534   flagval=flag;
    uvflag vis=$v line=channel,4,2601 flagval=flag;
    uvflag vis=$v line=channel,480,2604 flagval=flag;
    uvflag vis=$v line=channel,6,3083 flagval=flag;
echo "Did standard"
)
done
#========
