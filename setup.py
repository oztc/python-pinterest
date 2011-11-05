#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name="python-pinterest",
      version="0.1.0",
      description="Pinterest API client",
      license="MIT",
      install_requires=["simplejson"],
      author="Pinterest",
      author_email="api@pinterest.com",
      url="http://github.com/pinterest/python-pinterest",
      packages = find_packages(),
      keywords= "pinterest",
      zip_safe = True)


