#!/usr/bin/env python

from setuptools import setup

# jump through some hoops to get access to versionstring()
from sys import path
from os.path import abspath, dirname, join
topdir = abspath(dirname(__file__))
exec(open(join(topdir, "jvmlaunch/version.py"), "r").read())

# load contents of README.rst
readme = open("README.rst", "r").read()
    
setup(
    # package description
    name = "jvm-launch",
    version = versionstring(),
    description="manage JVM application startup",
    long_description=readme,
    author="Michael Frank",
    author_email="syntaxockey@gmail.com",
    url="https://github.com/msfrank/jvm-launch",
    # installation dependencies
    install_requires=[
        ],
    # package classifiers for PyPI
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License", 
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        ],
    # package contents
    packages=[
        "jvmlaunch",
        ],
    # distuils commands
    entry_points = {
        'console_scripts': [
            'jvm-launch=jvmlaunch.app:main',
            ]
        },
    # test configuration
    test_suite="test",
    tests_require=["nose >= 1.3.1"]
)
