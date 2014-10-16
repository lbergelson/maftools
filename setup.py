#!/usr/bin/env python

from setuptools import setup

setup(name='maftools',
      version='0.1',
      description='Mutation Annotation Format  tools',
      author='Louis Bergelson',
      author_email='louisb@broadinstitute.org',
      url='http://www.github.com/lbergelson/maftools/',
      packages=['maftools'],
      test_suite='nose.collector',
      tests_require=['nose'],
     )
