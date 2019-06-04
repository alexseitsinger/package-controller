import textwrap
import re

from ..generic.run import run
from ..generic.assert_which import assert_which
from .assert_repository import assert_repository
from .assert_commit_type import assert_commit_type
from .assert_commit_heading_length import assert_commit_heading_length
from .format_commit_text import format_commit_text
from .format_commit_description import format_commit_description


def commit(commit_type, subject, description=None):
    assert_repository()
    assert_which("git")
    assert_commit_type(commit_type)
    # Remove any excess whitespace from the subject.
    subject = format_commit_text(subject)
    # Create the heading for the commit.
    heading = "{}: {}".format(commit_type, subject)
    assert_commit_heading_length(heading)
    # Create the commit args.
    cmd = "git commit -m '{}'".format(heading)
    # Iterate over the description, if possible, and convert each line into
    # a new -m entry to use a newline in the commit message.
    if description is not None:
        formatted_description = format_commit_description(description)
        cmd = " ".join([cmd, "-m '{}'".format(formatted_description)])
    # Run the command we've put togehter to create the commit.
    run(cmd)
    last_commit_hash = run("git rev-parse HEAD")
    return last_commit_hash

