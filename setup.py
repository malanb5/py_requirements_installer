#!/usr/bin/env python

from setuptools import setup

setup(name='pyreqgen',
      version='1.0.1',
      description='Creates a requirements.txt file for a project '
				  'solely from source files, given a root directory',
      author='Matthew Bladek',
      author_email='malanb5@gmail.com',
	  url="https://github.com/malanb5/py_requirements_installer",
	  install_requires=['yaml>=5.2']
     )