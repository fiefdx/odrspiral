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

    print "#  OpenDRIVE spiral example"
    print "#  ------------------------\n#"
    print "#  Computing a spiral with"
    print "#    initial curvature =   0.000 1/m"
    print "#    length            = 300.000 m"
    print "#    curvDot           =   0.001 1/m2\n#"

    for s in xrange(0, 300, 1):
        x, y, t = odrspiral.spiral(s, 0.001, x, y, t)
        print "%10.4f %10.4f" % (x, y)
