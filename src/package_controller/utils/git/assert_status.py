from ..generic.run import run


def assert_status():
    status = run("git status -s")
    if status:
        raise AssertionError("There are uncommited changes.")

