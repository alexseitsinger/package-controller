import textwrap
import re

from .run import run
from .assert_which import assert_which
from .assert_commit_type import assert_commit_type
from .format_commit_text import format_commit_text
from .format_commit_description import format_commit_description

GIT_COMMIT_ARGS = ["git", "commit"]
GIT_LAST_COMMIT_HASH_ARGS = ["git", "rev-parse", "HEAD"]


def git_commit(commit_type, subject, description=None):
    assert_which("git")
    assert_commit_type(commit_type)
    # Remove any excess whitespace from the subject.
    subject = format_commit_text(subject)
    # Create the heading for the commit.
    heading = "{}: {}".format(commit_type, subject)
    heading_len = len(heading)
    heading_len_max = 50
    heading_len_diff = heading_len - heading_len_max
    if heading_len_diff > 0:
        raise RuntimeError("The heading is {} characters too long. "
                           "It must be {} characters or less.".format(
                           heading_len_diff, heading_len_max))
    # Create the commit args.
    commit_args = GIT_COMMIT_ARGS + ["-m", heading]
    # Iterate over the description, if possible, and convert each line into
    # a new -m entry to use a newline in the commit message.
    if description is not None:
        commit_args += ["-m", format_commit_description(description)]
    # Run the command we've put togehter to create the commit.
    run(*commit_args)
    # Then, get and return the hash for the commit we just created.
    return run(*GIT_LAST_COMMIT_HASH_ARGS)

