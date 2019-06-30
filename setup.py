#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages
from setup_utils import read, read_markdown

PACKAGE_NAME = "package-controller"
PACKAGE_ROOT_NAME = "package_controller"
GITHUB_URL = "https://github.com/alexseitsinger/{}".format(PACKAGE_NAME)
HOMEPAGE_URL = "https://www.alexseitsinger.com/packages/python/{}".format(PACKAGE_NAME)
README_NAME = "README.md"


setup(
    name=PACKAGE_NAME,
    version=read(("src", PACKAGE_ROOT_NAME, "__init__.py"), "__version__"),
    description=read_markdown((README_NAME,), "Description", (0,)),
    long_description=read((README_NAME,)),
    long_description_content_type="text/markdown",
    author="Alex Seitsinger",
    author_email="software@alexseitsinger.com",
    url=HOMEPAGE_URL,
    install_requires=["click", "semver", "toml", "requests"],
    entry_points={"console_scripts": ["pc={}.cli:main".format(PACKAGE_ROOT_NAME)]},
    package_dir={"": "src"},
    packages=find_packages("src", exclude=["tests"]),
    include_package_data=True,
    license="BSD 2-Clause License",
    keywords=["package", "semantic version", "git", "distribution"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
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
        "Documentation": HOMEPAGE_URL,
        "Source": GITHUB_URL,
        "Tracker": "{}/issues".format(GITHUB_URL),
    },
)
