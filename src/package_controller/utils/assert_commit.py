from subprocess import Popen, PIPE

GIT_LOG_ARGS = ["git", "log"]
GREP_ARGS = ["grep"]


def assert_commit(commit_hash):
    p1 = Popen(GIT_LOG_ARGS, stdout=PIPE)
    p2 = Popen(GREP_ARGS + [commit_hash], stdin=p1.stdout, stdout=PIPE, stderr=PIPE)
    p1.stdout.close()
    stdout, stderr = p2.communicate()
    if stdout.strip().decode("utf-8") == "commit {}".format(commit_hash):
        return True
    return False
