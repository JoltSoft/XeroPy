#/usr/bin/env python
from setuptools import setup, find_packages
import os

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

setup(
        name="XeroPy",
        description="Pythonic ORM implementation of the Xero API",
        zip_safe= False,
        version="1.3",
        packages = ['xero',],
        install_requires=[
            'httplib2>=0.6.0',
            'oauth2==1.2.0',
            'SocksiPy-branch==1.02',
            'python-dateutil',
            'M2Crypto',
            ],
        dependency_links=[
            'https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/socksipy-branch/SocksiPy-branch-1.02.tar.gz',
            ],
        )
