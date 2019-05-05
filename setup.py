#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from setup_utils import package_setup


package_setup(
    description="A simple package controller for automating setups, versioning, etc.",
    base_url="https://github.com/alexseitsinger",
    author="Alex Seitsinger",
    author_email="contact@alexseitsinger.com",
    install_requires=["click", "semver"],
    console_scripts={"pc": "cli:main"}
)

