# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from os import path
# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# packages required (replaces requirements.txt)
required = [
    'pandas>2.0',
    'scikit-survival',
    'seaborn'

]

setup(
    name="time_to_event",
    version="0.1",
    package_dir={'': 'src'},
    packages=["time_to_event"],
    py_modules=['time_to_event'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=required,
)
