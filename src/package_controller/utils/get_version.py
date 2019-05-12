import os

from .read_file import read_file
from .find_init_module import find_init_module


def get_version():
    init_module = find_init_module()
    version = read_file(init_module, "__version__")
    return version

