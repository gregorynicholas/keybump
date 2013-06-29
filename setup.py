#!/usr/bin/env python
"""
  keybump
  ~~~~~~~

  an opinionated script for managing + automating version releases in a github
  project. it makes following the semantic versioning specification a breeze.

  links
  -----

* [docs](http://gregorynicholas.github.io/keybump)
* [source](http://gregorynicholas.github.com/keybump)
* [package](http://packages.python.org/keybump)
* [semantic versioning specification](http://semver.org)

"""
from setuptools import setup

# setup the .keybump dir in the user home directory..
from os import path, makedirs
data_dir = path.expanduser("~/.keybump")
makedirs(data_dir)

with open("requirements.txt", "r") as f:
  required = f.readlines()

with open("README.md", "r") as f:
  long_description = f.read()


setup(
  name="keybump",
  version="3.0.1",
  url="http://github.com/gregorynicholas/keybump",
  license="MIT",
  author="gregorynicholas",
  author_email="gn@gregorynicholas.com",
  description=__doc__,
  long_description=long_description,
  py_modules=['keybump'],
  entry_points={
    "console_scripts": [
      'keybump = keybump:main',
    ]
  },
  zip_safe=False,
  platforms="any",
  install_requires=required,
  data_files=[
    (data_dir, [
      "data/.KEYBUMP_CHANGELOG_FMT",
      "data/.KEYBUMP_TAG_MSG_FMT",
    ])
  ],
  tests_require=[
    "mock==1.0.1",
  ],
  test_suite="keybump_tests",
  classifiers=[
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Python Modules'
  ]
)
