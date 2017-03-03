#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial import Polynomial as P
import scipy.signal as signal
from pylab import*
import h5py, katfile
import optparse
import shutil
from sys import stdout
import time

# This is a silly (but much more helpfull script) in 
# visually understanding the RFI.
# The idea is to implement the 'Detect_spikes' on the online RFI flagging system 

#----------------------------------------------------------------------------------
#--- FUNCTION :  detect_spikes_sumthreshold
#----------------------------------------------------------------------------------

def detect_spikes_sumthreshold(data, axis=1, spike_width=3, outlier_sigma=11.0, buffer_size=6, window_size=[2,4,8,16]):
    """
    Detect and Remove outliers from data, replacing them with a local median value.

    The data is median-filtered along the specified axis, and any data values
    that deviate significantly from the local median is replaced with the median
    to return the clean_data.

    Parameters
    ----------
    data : array-like
        N-dimensional numpy array containing data to clean
    axis : int, optional
        Axis along which to perform median, between 0 and N-1
    spike_width : int, optional
        Spikes with widths up to this limit (in samples) will be removed. A size
        of <= 0 implies no spike removal. The kernel size for the median filter
        will be 2 * spike_width + 1.
    outlier_sigma : float, optional
        Multiple of standard deviation that indicates an outlier
    buffer_size : int, optional
        The number of previous records to average in time.
    window_size : array of ints
        The size of the averaging windows to use for the sumthreshold method.

    Returns
    -------
    flag_array : array
        N-dimensional uint8 array of same shape as original data, with outliers
        removed

    Notes
    -----
    This is very similar to a *Hampel filter*, also known as a *decision-based
    filter* or three-sigma edit rule combined with a Hampel outlier identifier.

    This is an expanded version of the original MAD filter used in the online
    flagger that utilises the sumthreshold method described by Andre Offringa
    and used in the LOFAR flagger. See Offringa et al. MNRAS, 405, (2010) for
    details of the sumthreshold method.

    .. todo:

       TODO: Make this more like a Hampel filter by making MAD time-variable too.

    """
    
    flags = np.zeros(data.shape, dtype='uint8')
    kernel_size = 2 * max(int(spike_width), 0) + 1
    
    for ts_index in range(data.shape[0]):
	complete=float(ts_index)/float(data.shape[0])*100.0
        stdout.write("\r%3.1f%%" % complete)
        stdout.flush()
        for bl_index in range(data.shape[2]):
            subdata = data[ts_index:ts_index+buffer_size,:,bl_index]
            
            spectral_data = np.abs(subdata)
            spectral_data = np.atleast_1d(spectral_data)

            # Median filter data along the desired axis, with given kernel size
            kernel = np.ones(spectral_data.ndim, dtype='int32')
            kernel[axis] = kernel_size

            # Medfilt now seems to upcast 32-bit floats to doubles - convert it back to floats...
            filtered_data = np.asarray(signal.medfilt(spectral_data, kernel), spectral_data.dtype)
            
            # The deviation is measured relative to the local median in the signal
            dev = (spectral_data - filtered_data)
            
            # Average the current background subtracted buffer. 
            av_dev = np.average(dev[0:buffer_size],0)
            av_abs_dev = np.abs(av_dev)
            
            # Calculate median absolute deviation (MAD)
            med_abs_dev = np.median(av_abs_dev[av_abs_dev>0])
            # med_abs_dev = signal.medfilt(abs_dev, kernel)
            # Assuming normally distributed deviations, this is a robust estimator of the standard deviation
            estm_stdev = 1.4826 * med_abs_dev
            
            # Identify initial outliers (again based on normal assumption), and replace them with local median
            threshold = outlier_sigma * estm_stdev
            outliers = (av_dev > threshold)
            
            for window in window_size:
                #Set up 'this_data' from the averaged background subtracted buffer 
                bl_data = av_dev.copy()
                
                #The threshold for this iteration is calculated from the initial threshold
                #using the equation from Offringa (2010).
                # rho=1.2 in the equation seems to work better for KAT-7 than rho=1.5 from AO.
                thisthreshold = threshold / pow(1.2,(log(window)/log(2)))
                #Set already flagged values to be the value of this threshold
                bl_data[outliers] = thisthreshold
            
                #Calculate a rolling average array from the data with a windowsize for this iteration
                weight = np.repeat(1.0, window)/window
                avgarray = np.convolve(bl_data, weight,mode='valid')
                
                #Work out the flags from the convolved data using the current threshold.
                #Flags are padded with zeros to ensure the flag array (derived from the convolved data)
                #has the same dimension as the input data.
                this_flags = (avgarray > thisthreshold)

                #Convolve the flags to be of the same width as the current window.
                convwindow = np.ones(window,dtype=np.bool)
                this_outliers = np.convolve(this_flags,convwindow)
                
                #"OR" the flags with the flags from the previous iteration.
                outliers = outliers | this_outliers
                
            flags[ts_index,:,bl_index] = outliers
    # katfile wants flags to be uint8.
    return flags.astype(np.uint8)
    
parser = optparse.OptionParser(usage='prog[options]<data file>',
                description='This flags the rfi for the hdf5 file')

(opts, args) = parser.parse_args()

if len(args) < 1:
    print "Please specify the h5 file to be flagged."
    sys.exit(1)

f = h5py.File(args[0],mode='r+')
#print "Center Freq is", f.spectral_windows[f.spw].centre_freq*1e-6,"MHz"
# Data selection
corr_data = f['Data']['correlator_data'].value
data = corr_data.view(np.complex64)[:,:,:,0]
f.close()
#for threshold in np.arange(5,12,3):
#    for threshold in np.arange(5,12,3): 
#	spike_width
f =  h5py.File(args[0],mode='r+')
spike_width=8
threshold=11
start_time=time.time()
mask = detect_spikes_sumthreshold(data,spike_width=spike_width,outlier_sigma=threshold)
end_time=time.time()
#print "first few flags are", mask
# putting flags into file
del f['Markup']['flags']
f['Markup'].create_dataset('flags',data=mask)
obstime=f['Data']['timestamps'][-1] - f['Data']['timestamps'][0]
f.close()
print 
print "Observed in ",obstime, "seconds"
print
print "Executed in ",end_time - start_time, "seconds"
