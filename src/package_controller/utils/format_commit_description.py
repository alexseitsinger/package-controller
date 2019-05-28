import textwrap
import re

from .format_commit_text import format_commit_text

RE_DESCRIPTION_DELIMITER = r"(?![\w\d])\.\s+"


def format_commit_description(description):
    text = " ".join([
        format_commit_text(x)
        for x in re.split(RE_DESCRIPTION_DELIMITER, description)
        if len(x)
    ])
    return "\n".join(textwrap.wrap(text, width=72))

