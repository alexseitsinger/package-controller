from .add_file import add_file
from .assert_repository import assert_repository


def add(*files):
    assert_repository()
    if not len(files):
        raise RuntimeError("No files passed")
    return [add_file(x) for x in files]
