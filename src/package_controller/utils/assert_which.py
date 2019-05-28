from .which import which


def assert_which(name):
    if which(name) is None:
        raise RuntimeError("Executable not found. ({})".format(name))

