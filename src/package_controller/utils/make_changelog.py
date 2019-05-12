import os

from .run import run


def make_changelog(output="CHANGELOG.md", type="angular", style="angular"):
    run("git-changelog", ".", "-o", output, "-t", type, "-s", style)
    changelog = os.path.join(os.getcwd(), output)
    return changelog

