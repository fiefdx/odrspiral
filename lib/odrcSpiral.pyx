# -*- coding: utf-8 -*-
'''
Created on 2018-03-21
@summary:  odrspiral
@author: fiefdx
''' 
import numpy as np
cimport numpy as np

cimport odrSpirallink

def spiral(s, cDot, np.ndarray[np.float64_t, ndim=1] x, np.ndarray[np.float64_t, ndim=1] y, np.ndarray[np.float64_t, ndim=1] t):
    odrSpirallink.odrSpiral(<double> s, <double> cDot, <double*> x.data, <double*> y.data, <double*> t.data)