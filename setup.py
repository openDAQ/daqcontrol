#!/usr/bin/env python

from setuptools import setup


setup(
    name='daqcontrol',
    version='0.1',
    url='https://github.com/opendaq/daqcontrol',
    license='LGPL',
    author='Ingen10',
    install_requires=['pyserial', 'numpy', 'opendaq>=0.3.2'],
    author_email='ingen10@ingen10.com',
    description='A graphical user interface for openDAQ',
    packages=['daqcontrol'],
    platforms='any',
    entry_points={
        'gui_scripts': [
            'daqcontrol = daqcontrol.main:main',
        ]
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
