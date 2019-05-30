import os

from .find_file import find_file
from .is_git_repository import is_git_repository


def assert_git_repository(flat=False):
    if is_git_repository(flat=flat) is False:
        raise NotADirectoryError("A git repository was not detected within {} or it's ancestors.".format(path))
