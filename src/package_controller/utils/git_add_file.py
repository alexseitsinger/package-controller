import os

from .run import run
from .git_staged_file import git_staged_file


def git_add_file(f):
    try:
        run("git", "add", f)
        return f
    except RuntimeError as exc:
        msg = str(exc)
        # If we get a failed add due to unmatching file. attempt to find it.
        if msg.startswith("fatal: pathspec") and msg.endswith("did not match any files"):
            return git_add_file(git_staged_file(f))
        # Otehrwise, just raise the original exception.
        raise RuntimeError("Failed to add file {}".format(f))

