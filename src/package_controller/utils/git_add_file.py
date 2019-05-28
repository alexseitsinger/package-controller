import os

from .run import run
from .git_staged_files import git_staged_files

GIT_ADD_ARGS = ["git", "add"]


def git_add_file(f):
    try:
        run(*GIT_ADD_ARGS + [f])
        return f
    except RuntimeError as exc:
        msg = str(exc)
        # If we get a failed add due to unmatching file. attempt to find it.
        if msg.startswith("fatal: pathspec") and msg.endswith("did not match any files"):
            fn = os.path.basename(f)
            for sf in git_staged_files():
                if os.path.sep in f:
                    # path/to/dir/ -> path/to/dir/first.py, path/to/dir/second.py
                    if f.endswith(os.path.sep):
                        if sf.startswith(f):
                            return git_add_file(sf)
                    # path/to/file.py -> path/to/file.py
                    elif sf.endswith(f):
                        return git_add_file(sf)
                # file.py -> path/to/file.py 
                elif os.path.basename(sf) == fn:
                    return git_add_file(sf)
        # Otehrwise, just raise the original exception.
        raise RuntimeError("Failed to add file {}".format(f))

