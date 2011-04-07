#!/usr/bin/env python

import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='kalsel',
    version='0.1',
    description='Kalimantan Selatan Wetlands Calculations',
    author='Yus Budiyono',
    author_email='yus.budiyono@gmail.com',
    url='http://www.bppt.go.id/',
    packages=['kalsel',],
    install_requires=['shapely',
                      #'gdal'
          ], 
    license = "GPL",
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GPL License",
    ],
)
