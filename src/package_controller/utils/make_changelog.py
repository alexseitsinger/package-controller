import os

from .run import run
from .which import which


def make_changelog(output="CHANGELOG.md", changelog_type="angular", style="angular"):
    git_changelog = which("git-changelog")
    if git_changelog is None:
        raise RuntimeError("git-changelog is not installed.")
    run("git-changelog", ".", "-o", output, "-t", changelog_type, "-s", style)
    changelog = os.path.join(os.getcwd(), output)
    return changelog

