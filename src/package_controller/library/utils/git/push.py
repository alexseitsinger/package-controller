from ..run import run
from .assert_repository import assert_repository


COMMAND = "git push {force} {remote_name} {branch_name}"


def push(remote_name="origin", branch_name="master", tag_name=None, force=False):
    assert_repository()
    if force is True:
        run(
            COMMAND.format(force="-f", remote_name=remote_name, branch_name=branch_name)
        )
    else:
        run(COMMAND.format(force="", remote_name=remote_name, branch_name=branch_name))
    if tag_name is not None:
        run(COMMAND.format(force="", remote_name=remote_name, branch_name=tag_name))
