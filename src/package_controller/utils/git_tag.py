from .run import run


def git_tag(name, hash=None):
    if not name.startswith("v"):
        name = "v{}".format(name)
    args = ["git", "tag", name]
    if hash is not None:
        args.append(hash)
    return run(*args)

