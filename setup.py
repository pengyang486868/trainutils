#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='trainutils',
    version='0.4.2',
    description=(
        'simple train utils'
    ),
    long_description=open('README.rst').read(),
    author='Yang Peng',
    author_email='854525261@qq.com',
    maintainer='Yang Peng',
    maintainer_email='854525261@qq.com',
    license='BSD License',
    packages=find_packages(),
    include_package_data=True,
    platforms=["all"],
    url='https://github.com/pengyang486868',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[
        'numpy',
    ]
)
