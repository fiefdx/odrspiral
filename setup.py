# -*- coding: utf-8 -*-
'''
Created on 2018-03-21
@summary: opendrive spiral
@author: fiefdx
'''

from distutils.core import setup
from distutils.extension import Extension


from Cython.Distutils import build_ext
import numpy

kwargs = {}
kwargs["name"] = "odrspiral"
kwargs["version"] = "0.0.1"
kwargs["author"] = "fiefdx"
kwargs["author_email"] = "fiefdx@163.com"
kwargs["packages"] = ["odrspiral"]
kwargs["package_dir"] = {"odrspiral":"src"}

codrspiral = Extension(
    name = 'codrspiral',
    sources = ['lib/odrcSpiral.pyx', 'lib/odrSpirallink.pxd', 'lib/odrSpiral.c'],
    include_dirs = ['lib', numpy.get_include()]
)

kwargs["cmdclass"] = {'build_ext': build_ext}
kwargs["ext_modules"] = [codrspiral]

setup(**kwargs)