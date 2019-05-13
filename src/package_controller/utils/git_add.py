from .run import run

GIT_ADD_ARGS = ["git", "add"]

def git_add(*files):
    if not len(files):
        raise RuntimeError("No files passed")
    args = GIT_ADD_ARGS + list(files)
    return run(*args)

