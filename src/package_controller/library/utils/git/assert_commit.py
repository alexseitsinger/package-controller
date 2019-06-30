from subprocess import Popen, PIPE


def assert_commit(commit_hash):
    p1 = Popen(["git", "log"], stdout=PIPE)
    p2 = Popen(["grep", commit_hash], stdin=p1.stdout, stdout=PIPE, stderr=PIPE)
    p1.stdout.close()
    out, err = p2.communicate()
    if out.strip().decode("utf-8") != "commit {}".format(commit_hash):
        raise AssertionError("The commit {} does not exist.".format(commit_hash))
