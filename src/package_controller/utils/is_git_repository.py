import os

from .find_file import find_file


def is_git_repository(flat=False):
    try:
        git_dir = find_file(".git", flat=flat)
        if os.path.isdir(git_dir):
            return True
        return False
    except FileNotFoundError as exc:
        return False

