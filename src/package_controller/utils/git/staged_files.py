from subprocess import Popen, PIPE

from .assert_repository import assert_repository

GIT_STATUS_ARGS = ["git", "status", "-s"]
AWK_ARGS = ["awk", "{print $NF}"]


def staged_files():
    assert_repository()
    p1 = Popen(GIT_STATUS_ARGS, stdout=PIPE)
    p2 = Popen(AWK_ARGS, stdin=p1.stdout, stdout=PIPE, stderr=PIPE)
    p1.stdout.close()
    out, err = p2.communicate()
    return out.decode("utf-8").split()


