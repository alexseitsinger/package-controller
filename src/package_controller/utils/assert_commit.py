import subprocess


def assert_commit(hash):
    p1 = subprocess.Popen(["git", "log"], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["grep", hash], stdin=p1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p1.stdout.close()
    stdout, stderr = p2.communicate()
    if stdout.strip().decode("utf-8") == "commit {}".format(hash):
        return True
    return False
