from .run import run
from .git_staged_file import git_staged_file


def git_diff(f):
    staged_file = git_staged_file(f)
    if staged_file is None:
        raise FileNotFoundError(
            "Failed to find staged file matching {}".format(f))
    return run("git", "diff", staged_file)
