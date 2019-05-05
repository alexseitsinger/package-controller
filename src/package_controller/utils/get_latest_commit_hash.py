from .run import run


def get_latest_commit_hash():
    return run("git rev-parse HEAD")
