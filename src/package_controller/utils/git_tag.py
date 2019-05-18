from .run import run
from .assert_commit import assert_commit

GIT_TAG_ARGS = ["git", "tag"]


def git_tag(name, hash=None):
    if not name.startswith("v"):
        name = "v{}".format(name)
    args = GIT_TAG_ARGS + [name]
    if hash is not None:
        args.append(hash)
    try:
        return run(*args)
    except RuntimeError as exc:
        message = str(exc)
        # If we get some output and it says the tag exists, continue...
        if message.startswith("fatal: tag") and message.endswith("already exists"):
            # Get the commit hash that is connected to the tag.
            tagged_commit = run("git", "rev-list", "-n", str(1), name)
            # If the commit does not exist, then delete the tag, and re-run this command.
            # Otherwise, raise an exception.
            if not assert_commit(tagged_commit):
                run(*GIT_TAG_ARGS + ["-d", name])
                print("Deleting old tag that points to non-existant commit. ({}, {})".format(name, tagged_commit))
                return git_tag(name=name, hash=hash)
            else:
                raise RuntimeError("That tag already exists on a valid commit. ({}, {})".format(name, tagged_commit))
        else:
            raise exc


