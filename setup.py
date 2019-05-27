#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages
from setup_utils import DIRECTORY_NAME, PACKAGE_NAME, read, read_section

URL = "https://github.com/alexseitsinger/{}".format(PACKAGE_NAME)
README_NAME = "README.md"

setup(
    name=PACKAGE_NAME,
    version=read(("src", PACKAGE_NAME, "__init__.py",), "__version__"),
    description=read_section((README_NAME,), "Description", (0,)),
    long_description=read((README_NAME,)),
    long_description_content_type="text/markdown",
    author="Alex Seitsinger",
    author_email="contact@alexseitsinger.com",
    url=URL,
    install_requires=["click", "semver"],
    entry_points={"console_scripts": ["pc={}.cli:main".format(PACKAGE_NAME)]},
    package_dir={"": "src"},
    packages=find_packages("src", exclude=["tests"]),
    include_package_data=True,
    license="BSD 2-Clause License",
    keywords=["package", "semantic version", "git", "distribution"],
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Documentation",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Documentation",
        "Topic :: Software Development :: Version Control :: Git",
        "Topic :: System :: Archiving :: Packaging",
        "Topic :: System :: Software Distribution",
        "Topic :: Utilities",
        "Natural Language :: English",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Source": URL,
        "Tracker": "{}/issues".format(URL)
    }
)
