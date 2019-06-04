from ..generic.run import run
from .staged_file import staged_file
from .assert_repository import assert_repository


def diff(f):
    assert_repository()
    staged_file = staged_file(f)
    if staged_file is None:
        raise FileNotFoundError(
            "Failed to find staged file matching {}".format(f))
    return run("git diff {}".format(staged_file))
