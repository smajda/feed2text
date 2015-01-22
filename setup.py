#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="feed2text",
    version="0.0.1",
    author="Jon Smajda",
    description="Download feeds to markdown files",
    include_package_data=True,
    install_requires=[
        "click>=3.3",
        "feedparser==5.1.3",
        "html2text==2014.12.29",
    ],
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        feed2text=feed2text:cli
    ''',
)
