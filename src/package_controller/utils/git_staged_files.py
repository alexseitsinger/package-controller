from subprocess import Popen, PIPE

from .assert_git_repository import assert_git_repository

GIT_STATUS_ARGS = ["git", "status", "-s"]
AWK_ARGS = ["awk", "{print $NF}"]


def git_staged_files():
    assert_git_repository()
    p1 = Popen(GIT_STATUS_ARGS, stdout=PIPE)
    p2 = Popen(AWK_ARGS, stdin=p1.stdout, stdout=PIPE, stderr=PIPE)
    p1.stdout.close()
    out, err = p2.communicate()
    return out.decode("utf-8").split()


