from .run import run

GIT_STATUS_ARGS = ["git", "status", "-s"]


def assert_status():
    status = run(*GIT_STATUS_ARGS)
    if status:
        raise RuntimeError("There are uncommited changes")

