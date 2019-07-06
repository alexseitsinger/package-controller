from ..utils.run import run
from ..utils.git.assert_repository import assert_repository


CMD = "git rebase -i {}"


def resave(count):
    assert_repository()
    if count == "all":
        cmd = CMD.format("--root")
    elif not isinstance(count, int):
        raise RuntimeError("Count must be either 'all' or an integer.")
    if count == 1:
        cmd = CMD.format("HEAD^")
    else:
        cmd = CMD.format("HEAD~{}".format(count))
    return run(cmd)
