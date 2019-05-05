import os

from .read_file import read_file
from .find_init_module import find_init_module
from ..settings import DEFAULT_VERSION_VARIABLE


def get_package_version(variable=DEFAULT_VERSION_VARIABLE):
    init_module = find_init_module()
    package_version = read_file(init_module, variable)
    return package_version

