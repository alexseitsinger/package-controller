import os

from .run import run
from .git_staged_file import git_staged_file
from .assert_git_repository import assert_git_repository


def git_add_file(f):
    assert_git_repository()
    if f is None:
        raise IOError("A file name or path is required.")
    try:
        run("git add {}".format(f))
        return f
    except RuntimeError as exc:
        msg = str(exc)
        # If we get a failed add due to unmatching file. attempt to find it.
        if msg.startswith("fatal: pathspec") and msg.endswith("did not match any files"):
            sf = git_staged_file(f)
            if sf:
                return git_add_file(sf)
        # Otehrwise, just raise the original exception.
        raise RuntimeError("Failed to add file {}".format(f))

