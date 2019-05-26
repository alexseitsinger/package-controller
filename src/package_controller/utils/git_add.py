from .run import run

GIT_ADD_ARGS = ["git", "add"]


def git_add(*files):
    if not len(files):
        raise RuntimeError("No files passed")
    return run(*GIT_ADD_ARGS + list(files))

