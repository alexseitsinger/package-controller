from .run import run

GIT_PUSH_ARGS = ["git", "push"]


def git_push(remote="origin", branch="master", tags=False):
    if tags is True:
        args = GIT_PUSH_ARGS + ["--tags"]
    else:
        args = GIT_PUSH_ARGS + [remote, branch]
    return run(*args)

