#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

from django_moment import __version__


setup(
    name='django-moment',
    version=__version__,
    author='Hannes Gräuler',
    author_email='hannes@smasi.de',
    description='Django real-time analytics powered by redis-moment',
    url='https://github.com/lordi/django-moment',
    packages=find_packages(),
    install_requires=[
        'redis',
        'redis-moment'
    ],
    zip_safe=False,
    include_package_data=True,
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: System :: Distributed Computing',
        'Topic :: Software Development :: Object Brokering',
    ]
)
