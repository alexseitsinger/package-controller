import os

from .run import run
from subprocess import Popen, PIPE

GIT_STATUS_ARGS = ["git", "status", "-s"]
GIT_ADD_ARGS = ["git", "add"]
AWK_ARGS = ["awk", "{print $NF}"]


def _list_staged_files():
    p1 = Popen(GIT_STATUS_ARGS, stdout=PIPE)
    p2 = Popen(AWK_ARGS, stdin=p1.stdout, stdout=PIPE, stderr=PIPE)
    p1.stdout.close()
    out, err = p2.communicate()
    return out.decode("utf-8").split()


def _add_file(f):
    try:
        run(*GIT_ADD_ARGS + [f])
        return f
    except RuntimeError as exc:
        msg = str(exc)
        # If we get a failed add due to unmatching file. attempt to find it.
        if msg.startswith("fatal: pathspec") and msg.endswith("did not match any files"):
            for sf in _list_staged_files():
                if os.path.sep in f:
                    # path/to/dir/ -> path/to/dir/first.py, path/to/dir/second.py
                    if f.endswith(os.path.sep):
                        if sf.startswith(f):
                            return _add_file(sf)
                    # path/to/file.py -> path/to/file.py
                    elif sf.endswith(f):
                        return _add_file(sf)
                # file.py -> path/to/file.py 
                elif os.path.basename(sf) == os.path.basename(f):
                    return _add_file(sf)
        # Otehrwise, just raise the original exception.
        raise RuntimeError("Failed to add file {}".format(f))


def git_add(*files):
    if not len(files):
        raise RuntimeError("No files passed")
    return [ _add_file(x) for x in files ]
