#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import re
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))
NAME = os.path.basename(HERE)


def read(*parts):
    with open(os.path.join(HERE, *parts), "r", encoding="utf-8") as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name=NAME,
    version=find_version("src", NAME, "__init__.py"),
    description="",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/alexseitsinger/{}".format(NAME),
    author="Alex Seitsinger",
    author_email="contact@alexseitsinger.com",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
    ],
    package_dir={"": "src"},
    packages=find_packages("src", exclude=["tests"]),
    license="BSD 2-Clause License",
    install_requires=[],
    include_package_data=True,
)
