# -*- coding: utf-8 -*-
'''
Created on 2018-03-21
@summary: test
@author: fiefdx
'''

from odrspiral import odrspiral

if __name__ == "__main__":
    x = 0.0
    y = 0.0
    t = 0.0
    for s in xrange(0, 300, 1):
        x, y, t = odrspiral.spiral(s, 0.001, x, y, t)
        print "%10.4f %10.4f" % (x, y)
