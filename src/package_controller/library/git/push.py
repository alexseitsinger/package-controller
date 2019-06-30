from ..generic.run import run
from .assert_repository import assert_repository


COMMAND = "git push {force} {remote} {branch}"


def push(remote="origin", branch="master", tag=None, force=False):
    assert_repository()
    if force is True:
        run(COMMAND.format(force="-f", remote=remote, branch=branch))
    else:
        run(COMMAND.format(force="", remote=remote, branch=branch))
    if tag is not None:
        run(COMMAND.format(force="", remote=remote, branch=tag))
