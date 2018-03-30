# -*- coding: utf-8 -*-
'''
Created on 2018-03-21
@summary: odrSpiral.pxd for odrspiral C lib
@author: fiefdx
''' 

cdef extern from "odrSpiral.h":
    void odrSpiral(double s, double cDot, double *x, double *y, double *t);