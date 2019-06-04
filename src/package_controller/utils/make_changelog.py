import os

from .run import run
from .which import which
from .assert_git_repository import assert_git_repository
from .assert_git_remotes import assert_git_remotes
from .assert_which import assert_which


def make_changelog(changelog_output="CHANGELOG.md", changelog_type="angular", changelog_style="angular"):
    assert_git_repository()
    assert_git_remotes()
    assert_which("git-changelog")
    run("git-changelog . -o {changelog_output} -t {changelog_type} -s {changelog_style}".format(
        changelog_output=changelog_output,
        changelog_type=changelog_type,
        changelog_style=changelog_style,
    ))
    changelog_path = os.path.join(os.getcwd(), changelog_output)
    return changelog_path

