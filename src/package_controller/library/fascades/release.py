from ..git.push import push
from ..git.create_release import create_release
from ..git.get_latest_changelog import get_latest_changelog
from ..fascades.version import version


def release(remote="origin", branch="master", force=False):
    # Get the tag name if we're creating one.
    tag = "v{}".format(version())
    # Push our changes.
    push(remote, branch, tag, force)
    # Create a new release on GitHUb for the tag we just created.
    changelog = get_latest_changelog(tag)
    create_release(tag, changelog)
