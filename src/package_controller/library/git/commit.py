import textwrap
import re

from ..generic.run import run
from ..generic.assert_which import assert_which
from .assert_repository import assert_repository
from .assert_commit_type import assert_commit_type
from .assert_commit_heading_length import assert_commit_heading_length
from .format_commit_text import format_commit_text
from .format_commit_description import format_commit_description


def get_commit_messages(commit_type, message):
    bits = message.split(". ", 1)
    subject = bits.pop(0)
    heading = "{}: {}".format(commit_type, format_commit_text(subject))
    assert_commit_heading_length(heading)
    if len(bits):
        description = format_commit_description(". ".join(bits))
    else:
        description = ""
    return [heading, description]


def commit(commit_type, message):
    assert_repository()
    assert_which("git")
    assert_commit_type(commit_type)
    heading, description = get_commit_messages(commit_type, message)
    cmd = "git commit -m '{}'".format(heading)
    if len(description):
        cmd += " -m '{}'".format(description)
    run(cmd)
    last_commit_hash = run("git rev-parse HEAD")
    return last_commit_hash
