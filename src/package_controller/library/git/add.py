from .add_file import add_file
from .assert_repository import assert_repository


def add(*files):
    assert_repository()
    if len(files) == 0:
        return [add_file()]
    else:
        return [add_file(x) for x in files]
