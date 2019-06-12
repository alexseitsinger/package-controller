from subprocess import Popen, PIPE

from .which import which
from ..python.is_python_package import is_python_package


def assert_which(name):
    if which(name) is None:
        if is_python_package():
            p1 = Popen(["pipenv", "graph"], stdout=PIPE, stderr=PIPE)
            p2 = Popen(["grep", name], stdin=p1.stdout, stdout=PIPE, stderr=PIPE)
            p1.stdout.close()
            out, err = p2.communicate()
            if len(out.decode("utf-8")):
                return None
        raise AssertionError("Executable was not found. ({})".format(name))
