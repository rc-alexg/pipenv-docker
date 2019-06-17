#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
test with::

    python setup.py build_ext --inplace

create wheels with wheel installed::

    python setup.py bdist_wheel
    python setup.py sdist --formats=gztar

Note: install yaml in advance to get compiled acceleration

On MacOS::

    brew install libyaml
'''

from setuptools import setup
# from Cython.Build import cythonize

setup(name='examp',
      packages=["src"],
      install_requires=["flask", "python-dateutil"])