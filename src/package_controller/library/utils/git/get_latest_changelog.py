import re

from ..run import run


def get_latest_changelog(tag_name):
    cmd = "git-changelog -t angular -s angular ."
    out = run(cmd)
    section = out.split("\n\n\n")[0]
    try:
        heading, body = section.split("\n\n", 1)
        repl_heading = re.sub(r"v(\.?\d+)+", tag_name, heading)
        return "\n\n".join([repl_heading, body])
    except ValueError:
        return section
