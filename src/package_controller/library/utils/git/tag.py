import re

from ..run import run
from .assert_commit import assert_commit
from .assert_repository import assert_repository


def tag(name, commit_hash=None):
    assert_repository()
    # Make sure the tag name is formatted correctly.
    if not name.startswith("v"):
        name = "v{}".format(name)
    cmd = "git tag {}".format(name)
    if commit_hash is not None:
        cmd += " {}".format(commit_hash)
    # Try to run the git tag command.
    # If it succeeds, return the commit hash and the tag name in a tuple.
    # If it fails, and its due to a tag already existing, try to replace it
    # if its associated to a non-existant commit.
    # Otherwise, raise an exception.
    try:
        run(cmd)
        return (commit_hash, name)
    except RuntimeError as exc:
        msg = str(exc)
        # If we get some output and it says the tag exists, continue.
        if msg.startswith("fatal: tag") and msg.endswith("already exists"):
            # Get the commit hash that is connected to the tag.
            tagged_commit = run("git rev-list -n {} {}".format(str(1), name))
            # If the commit does not exist, then delete the tag, and re-run this command.
            try:
                assert_commit(tagged_commit)
                raise RuntimeError(
                    "The tag {} already exists on the commit {}.".format(
                        name, tagged_commit
                    )
                )
            except AssertionError as exc:
                print(
                    "Deleting the tag {} that points to the non-existant commit {}.".format(
                        name, tagged_commit
                    )
                )
                run("git tag -d {}".format(name))
                return tag(name, commit_hash)
        raise exc
