from subprocess import Popen, PIPE

GIT_LOG_ARGS = ["git", "log"]
GREP_ARGS = ["grep"]


def assert_commit(hash):
    p1 = Popen(GIT_LOG_ARGS, stdout=PIPE)
    p2 = Popen(GREP_ARGS + [hash], stdin=p1.stdout, stdout=PIPE, stderr=PIPE)
    p1.stdout.close()
    stdout, stderr = p2.communicate()
    if stdout.strip().decode("utf-8") == "commit {}".format(hash):
        return True
    return False
