#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup


def publish():
    """Publish to PyPi"""
    os.system("python setup.py sdist upload")


if sys.argv[-1] == "publish":
    publish()
    sys.exit()

required = []

setup(
    name='pyandoc',
    version='0.0.3',
    description='Python wrapper for Pandoc - the universal document converter',
    long_description=open('README.rst').read() + '\n\n' +
                     open('HISTORY.rst').read(),
    author='Kenneth Reitz, Martin Martimeo',
    author_email='me@kennethreitz.com, martin@martimeo.de',
    url='http://github.com/kennethreitz/pyandoc',
    packages=[
        'pandoc',
    ],
    install_requires=required,
    license='MIT',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    ),
    # entry_points={
    #   'console_scripts': [
    #       'tabbed = tablib.cli:start',
    #   ],
    # }
)
