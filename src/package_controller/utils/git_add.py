from .run import run


def git_add(*files):
    if not len(files):
        raise RuntimeError("No files passed")
    args = ["git", "add"] + list(files)
    return run(*args)

