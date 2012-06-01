#!/usr/bin/env python

try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup

setup(
    name='Djamboloader',
    version='0.1.0',
    description='A python/django based combo loader for javascript and css',
    long_description='djamboloader (for django combo loader) is a simple django application used to load and combine a list of javascript or css files from the filesystem for a specific library.',
    author='Julien Lauron',
    url='https://github.com/jlauron/djamboloader',
    download_url='https://github.com/jlauron/djamboloader/downloads',
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
    packages=[
        'djamboloader',
        'djamboloader.util',
    ],
)
