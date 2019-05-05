from .run import run
from .get_latest_commit_hash import get_latest_commit_hash


def assert_latest_commit_tag():
    latest_commit_hash = get_latest_commit_hash()
    command = "git describe --tags --exact-match {}".format(latest_commit_hash)
    try:
        out = run(command)
        return True
    except RuntimeError:
        return False
