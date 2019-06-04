from .run import run
from .assert_git_repository import assert_git_repository


def git_push(remote="origin", branch="master", tag_name=None):
    assert_git_repository()
    run("git push {} {}".format(remote, branch))
    if tag_name is not None:
        run("git push {} {}".format(remote, tag_name))

