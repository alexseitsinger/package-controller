from .git_add_file import git_add_file


def git_add(*files):
    if not len(files):
        raise RuntimeError("No files passed")
    return [git_add_file(x) for x in files]
