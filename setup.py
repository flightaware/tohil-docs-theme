#!/usr/bin/env python

import io

from setuptools import setup

# README into long description
with io.open('README.rst', encoding='utf-8') as readme_file:
    long_description = readme_file.read()


setup(
    name='tohil-docs-theme',
    # Version is date based as year.month[.serial], where serial is used
    # if multiple releases are needed to address build failures.
    version='2021.5.dev',
    description='The Sphinx theme for the CPython docs and related projects',
    long_description=long_description,
    author='FlightAware Developers',
    author_email='noreply@flightaware.com',
    url='https://github.com/flightaware/tohil-docs-theme/',
    packages=['tohil_docs_theme'],
    include_package_data=True,
    entry_points={
        'sphinx.html_themes': [
            'tohil_docs_theme = tohil_docs_theme',
        ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
