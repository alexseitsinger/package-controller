from .git_add_file import git_add_file
from .assert_git_repository import assert_git_repository


def git_add(*files):
    assert_git_repository()
    if not len(files):
        raise RuntimeError("No files passed")
    return [git_add_file(x) for x in files]
