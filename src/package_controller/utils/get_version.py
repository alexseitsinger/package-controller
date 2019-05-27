import os

from .read_file import read_file
from .find_init_module import find_init_module


def get_version():
    return read_file(find_init_module(), "__version__")

