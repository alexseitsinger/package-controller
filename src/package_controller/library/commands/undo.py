from ..utils.run import run
from ..utils.git.assert_repository import assert_repository

CMD = "git reset HEAD{} --hard"


def undo(count):
    assert_repository()
    if not isinstance(count, int):
        raise RuntimeError("Count must be an integer.")
    if count == 1:
        cmd = CMD.format("^")
    else:
        cmd = CMD.format("~{}".format(count))
    return run(cmd)
