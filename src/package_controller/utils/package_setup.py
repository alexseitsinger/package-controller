import os
from setuptools import find_packages, setup

from .get_package_version import get_package_version
from .find_file import find_file
from .get_package_long_description import get_package_long_description


def package_setup(*args, **kwargs):
    setup_file = find_file("setup.py")
    root_dir = os.path.dirname(setup_file)

    name = kwargs.pop("name", os.path.basename(root_dir))

    entry_points = {}
    console_scripts = kwargs.pop("console_scripts", None)
    if console_scripts is not None:
        entry_points["console_scripts"] = []
        for key, value in console_scripts.items():
            entry_points["console_scripts"].append(
                "{}={}.{}".format(key, name, value)
            )

    classifiers = list(set(kwargs.pop("classifiers", []) + [
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
    ]))

    base_url = kwargs.pop("base_url")
    url = "/".join([base_url, name])

    return setup(
        name=name,
        version=get_package_version(),
        long_description=get_package_long_description(),
        long_description_content_type="text/markdown",
        url=url,
        classifiers=classifiers,
        package_dir={"": "src"},
        packages=find_packages("src", exclude=["tests"]),
        license="BSD 2-Clause License",
        entry_points=entry_points,
        include_package_data=True,
        *args,
        **kwargs,
    )

