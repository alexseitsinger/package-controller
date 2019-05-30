from .run import run
from .assert_git_repository import assert_git_repository

GIT_PUSH_ARGS = ["git", "push"]
GIT_PUSH_TAGS_ARGS = ["--tags"]


def git_push(remote="origin", branch="master", tags=False):
    assert_git_repository()
    if tags is True:
        args = GIT_PUSH_ARGS + GIT_PUSH_TAGS_ARGS
    else:
        args = GIT_PUSH_ARGS + [remote, branch]
    return run(*args)

