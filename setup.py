#!/usr/bin/env python

from setuptools import setup
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_version():
    path = os.path.join(BASE_DIR, 'drift_api', '__init__.py')
    version_line = None
    with open(path) as fp:
        for line in fp:
            if line.startswith('__version__'):
                version_line = line
                break

    if not version_line:
        raise ValueError('Unable to find version line in __init__.py')

    version = version_line.split('=')[1].strip().strip("'")
    return version


def long_description():
    """Get the long description from the README"""
    return open(os.path.join(BASE_DIR, 'README.rst')).read()


setup(
    name='drift-api',
    version=get_version(),
    description='A wrapper for the Drift API',
    url='https://github.com/15five/drift-api',
    download_url='https://github.com/15five/drift-api/archive/master.zip',
    author='Paul Logston',
    author_email='paul@15five.com',
    keywords='drift http api',
    license='MIT',
    long_description=long_description(),
    packages=['drift_api'],
    install_requires=[
        'requests>=2.0.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

