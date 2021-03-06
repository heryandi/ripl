#!/usr/bin/env python
'''Setuptools params'''

from setuptools import setup, find_packages

setup(
    name='ripl',
    version='0.0.0',
    description='Library for data center networks',
    author='Brandon Heller',
    author_email='brandonh@stanford.edu',
    packages=find_packages(exclude='test'),
    long_description=open('README').read(),
    classifiers=[
        "Mininet :: Module :: Topology",
        "Mininet :: Module :: Others",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Internet",
    ],
    keywords='networking protocol Internet OpenFlow data center datacenter',
    license='GPL',
    install_requires=[
        'setuptools',
        'mininet',
        'networkx'
    ]
)
