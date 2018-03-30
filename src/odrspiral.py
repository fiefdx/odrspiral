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
    x = np.double(x)
    y = np.double(y)
    t = np.double(t)
    xyt = np.ascontiguousarray([x, y, t], dtype = np.float64)
    codrspiral.spiral(xyt, s, cdot)
    return xyt[0], xyt[1], xyt[2]
