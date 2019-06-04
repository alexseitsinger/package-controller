from ..generic.run import run
from .staged_file import staged_file
from .assert_repository import assert_repository


def diff(f):
    assert_repository()
    sf = staged_file(f)
    if sf is None:
        raise FileNotFoundError(
            "Failed to find staged file matching {}".format(f))
    return run("git diff {}".format(sf))
