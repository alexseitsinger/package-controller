from .run import run


GIT_TAG_ARGS = ["git", "tag"]

def git_tag(name, hash=None):
    if not name.startswith("v"):
        name = "v{}".format(name)
    args = GIT_TAG_ARGS + [name]
    if hash is not None:
        args.append(hash)
    return run(*args)

