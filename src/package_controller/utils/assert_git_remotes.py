from .run import run


def assert_git_remotes():
    remotes = run("git remote").strip()
    if not len(remotes):
        raise AssertionError("No git remotes detected.")

