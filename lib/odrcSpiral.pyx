# -*- coding: utf-8 -*-
'''
Created on 2018-03-21
@summary:  odrspiral
@author: fiefdx
''' 
import numpy as np
cimport numpy as np

cimport odrSpirallink

def spiral(np.ndarray[np.float64_t, ndim=1] xyt, s, cDot):
    odrSpirallink.odrSpiral(<double*> xyt.data, <double> s, <double> cDot)