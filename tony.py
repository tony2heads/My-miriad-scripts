
import katdal
import numpy as np
import matplotlib.pylab as plt

import katcal
from katcal import calprocs

# ------------------------------------------------------------------------
# open file
file_name = '/data1/NASSP/reduction_script/1355292163.h5'
f = katdal.open(file_name)
# select polarisation
#  solver can only work on one polarisation at a time in this framework
f.select(pol='h')

# get info that is needed for the solver
antlist = [a.name for a in f.ants]
corr_products = f.corr_products
antlist1, antlist2 = calprocs.get_solver_antlists(antlist,corr_products)

# ------------------------------------------------------------------------
# solve for gains

glist = []
tlist = []

for scan_ind, scan_state, target in f.scans():     
    if 'track' in scan_state and 'gaincal' in target.tags:

        vis = f.vis[:]
        times = f.timestamps[:]

        # average all channels together
        ave_vis = np.average(vis,axis=1)
        # solve for gains for every timestamp
        gsoln = calprocs.g_fit(ave_vis,antlist1,antlist2,g0=None,refant=1,algorithm='adi')

        for g in gsoln: glist.append(g)
        for t in times: tlist.append(t)

abs_g = np.abs(np.squeeze(glist))
phase_g = np.angle(np.squeeze(glist))
t = np.squeeze(tlist)

# plot gains
plt.subplot(211)
plt.plot(t,abs_g,'.')
plt.subplot(212)
plt.plot(t,180.*phase_g/np.pi,'.')
plt.show()

# ------------------------------------------------------------------------
# solve for bandpasses 

bplist = []
tlist = []

for scan_ind, scan_state, target in f.scans(): 
        
    if 'track' in scan_state and 'bpcal' in target.tags:

        vis = f.vis[:]
        times = f.timestamps[:]
         
        # average all times in this scan together
        ave_vis = np.average(vis,axis=0)
        # solve for bandpass
        bpsoln = calprocs.bp_fit(ave_vis,antlist1,antlist2,bp0=None,refant=1,algorithm='adi')

        bplist.append(bpsoln)
        tlist.append(np.average(t))

abs_bp = np.abs(np.squeeze(bplist))
t = np.squeeze(tlist)

# plot bp for each bp scan
for ti in t:
   for bp in abs_bp.T:
      plt.plot(bp)
   plt.show()


