from ..generic.run import run
from .assert_repository import assert_repository


def push(remote="origin", branch="master", tag_name=None):
    assert_repository()
    run("git push {} {}".format(remote, branch))
    if tag_name is not None:
        run("git push {} {}".format(remote, tag_name))

