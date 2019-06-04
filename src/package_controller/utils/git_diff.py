from .run import run
from .git_staged_file import git_staged_file
from .assert_git_repository import assert_git_repository


def git_diff(f):
    assert_git_repository()
    staged_file = git_staged_file(f)
    if staged_file is None:
        raise FileNotFoundError(
            "Failed to find staged file matching {}".format(f))
    return run("git diff {}".format(staged_file))
