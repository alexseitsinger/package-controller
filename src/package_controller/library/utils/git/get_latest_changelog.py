import re

from ..read_file import read_file


def get_latest_changelog():
    out = read_file("CHANGELOG.md")
    section = out.split("\n\n\n")[0]
    try:
        heading, body = section.split("\n\n", 1)
        return body
    except ValueError:
        return section
