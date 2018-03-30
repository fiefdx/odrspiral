# -*- coding: utf-8 -*-
'''
Created on 2018-03-21
@summary: odrSpiral.pxd for odrspiral C lib
@author: fiefdx
''' 

cdef extern from "odrSpiral.h":
    void odrSpiral(double* xyt, double s, double cDot);