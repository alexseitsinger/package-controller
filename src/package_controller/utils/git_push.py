from .run import run

GIT_PUSH_ARGS = ["git", "push"]
GIT_PUSH_TAGS_ARGS = ["--tags"]

def git_push(remote="origin", branch="master", tags=False):
    if tags is True:
        args = GIT_PUSH_ARGS + GIT_PUSH_TAGS_ARGS
    else:
        args = GIT_PUSH_ARGS + [remote, branch]
    return run(*args)

