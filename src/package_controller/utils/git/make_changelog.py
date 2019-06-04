import os

from .assert_repository import assert_repository
from .assert_remotes import assert_remotes
from ..generic.assert_which import assert_which
from ..generic.run import run


def make_changelog(changelog_output="CHANGELOG.md", changelog_type="angular", changelog_style="angular"):
    assert_repository()
    assert_remotes()
    assert_which("git-changelog")
    run("git-changelog . -o {changelog_output} -t {changelog_type} -s {changelog_style}".format(
        changelog_output=changelog_output,
        changelog_type=changelog_type,
        changelog_style=changelog_style,
    ))
    changelog_path = os.path.join(os.getcwd(), changelog_output)
    return changelog_path

