import os

from .is_repository import is_repository
from ..generic.find_file import find_file


def assert_repository(flat=False):
    if is_repository(flat=flat) is False:
        raise AssertionError("A git repository was not detected.")
