import semver

from .git_status import git_status
from .get_version import get_version
from .save_version import save_version


def bump_version(major=False, minor=False, patch=False):
    git_status()
    current_version = get_version()
    next_version = None
    if major is True and all([x is False for x in [minor, patch]]):
        next_version = semver.bump_major(current_version)
    elif minor is True and all([x is False for x in [major, patch]]):
        next_version = semver.bump_minor(current_version)
    elif patch is True and all([x is False for x in [major, minor]]):
        next_version = semver.bump_patch(current_version)
    if next_version is None:
        raise RuntimeError("Can only update one of major, minor, or patch")
    save_version(next_version)
    return (current_version, next_version,)

