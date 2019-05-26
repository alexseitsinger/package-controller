import os

from .run import run
from subprocess import Popen, PIPE

GIT_STATUS_ARGS = ["git", "status", "-s"]
GIT_ADD_ARGS = ["git", "add"]
AWK_ARGS = ["awk", "{print $NF}"]


def get_staged_files():
    p1 = Popen(GIT_STATUS_ARGS, stdout=PIPE)
    p2 = Popen(AWK_ARGS, stdin=p1.stdout, stdout=PIPE, stderr=PIPE)
    p1.stdout.close()
    out, err = p2.communicate()
    decoded = out.decode("utf-8")
    split = decoded.split()
    return split


def git_add_file(f):
    try:
        run(*GIT_ADD_ARGS + [f])
        # Return the successful add file name.
        return f
    except RuntimeError as exc:
        message = str(exc)
        # If we get a failed add due to unmatching file. attempt to find it.
        if message.startswith("fatal: pathspec") and message.endswith("did not match any files"):
            for sf in get_staged_files():
                # If we get a relative path, compare the end of the string.
                if len(f.split(os.path.sep)) > 1 and sf.endswith(f):
                    return git_add_file(sf)
                # Otehrwise, compare basenames of files.
                elif os.path.basename(sf) == os.path.basename(f):
                    return git_add_file(sf)
        # Otehrwise, just raise the original exception.
        raise exc


def git_add(*files):
    if not len(files):
        raise RuntimeError("No files passed")
    succeeded = []
    for f in list(files):
        fn = git_add_file(f)
        if fn is not None:
            succeeded += [fn]
    return succeeded
