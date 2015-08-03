#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import djjsoneditor

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-json-editor',
    version='0.1.0',
    description="""A powerful json web editor for django""",
    long_description=readme + '\n\n' + history,
    author='Leo Zhou',
    author_email='glasslion@gmail.com',
    url='https://github.com/glasslion/django-json-editor',
    packages=[
        'djjsoneditor',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-json-editor',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
