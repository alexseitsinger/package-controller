from .which import which


def assert_which(name):
    if which(name) is None:
        raise AssertionError("Executable was not found. ({})".format(name))

