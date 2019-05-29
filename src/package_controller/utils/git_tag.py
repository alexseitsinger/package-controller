from .run import run
from .assert_commit import assert_commit

GIT_TAG_ARGS = ["git", "tag"]

def git_tag(name, commit_hash=None):
    # Make sure the tag name is formatted correctly.
    if not name.startswith("v"):
        name = "v{}".format(name)
    # Create the args we're going to use.
    args = GIT_TAG_ARGS + [name]
    if commit_hash is not None:
        args += [commit_hash]
    # Try to run the git tag command.
    # If it succeeds, return the commit hash and the tag name in a tuple.
    # If it fails, and its due to a tag already existing, try to replace it
    # if its associated to a non-existant commit.
    # Otherwise, raise an exception.
    try:
        run(*args)
        return (commit_hash, name,)
    except RuntimeError as exc:
        msg = str(exc)
        # If we get some output and it says the tag exists, continue.
        if msg == "fatal: tag '{}' already exists".format(name):
            # Get the commit hash that is connected to the tag.
            tagged_commit = run("git", "rev-list", "-n", str(1), name)
            # If the commit does not exist, then delete the tag, and re-run this command.
            try:
                assert_commit(tagged_commit)
                raise RuntimeError("The tag {} already exists on the commit {}.".format(name, tagged_commit))
            except AssertionError as exc:
                print("Deleting the tag {} that points to the non-existant commit {}.".format(name, tagged_commit))
                run(*GIT_TAG_ARGS + ["-d", name])
                return git_tag(name, commit_hash)
        raise exc


