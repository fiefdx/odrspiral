# -*- coding: utf-8 -*-
'''
Created on 2018-03-21
@summary: opendrive spiral
@author: fiefdx
'''

import logging

import numpy as np

import codrspiral

LOG = logging.getLogger(__name__)


def spiral(s, cdot, x, y, t):
    s = np.double(s)
    cdot = np.double(cdot)
    x = np.ascontiguousarray([np.double(x)], dtype = np.float64)
    y = np.ascontiguousarray([np.double(y)], dtype = np.float64)
    t = np.ascontiguousarray([np.double(t)], dtype = np.float64)
    codrspiral.spiral(s, cdot, x, y, t)
    return x, y, t
