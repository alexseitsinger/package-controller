import semver

from .assert_status import assert_status
from .get_version import get_version
from .save_version import save_version
from .assert_which import assert_which
from .find_file import find_file
from .run import run
from .is_python_package import is_python_package
from .is_node_package import is_node_package


def bump_version_python(old_version, new_version):
    assert_which("python")
    save_version(new_version)
    return (old_version, new_version,)


def bump_version_node(old_version, new_version):
    assert_which("node")
    assert_which("yarn")
    # update the version...
    run("yarn", "version", "--new-version", new_version, "--message", new_version)
    # return the version numbers.
    return (old_version, new_version,)


def bump_version(major=False, minor=False, patch=False, force=False):
    if force is False:
        assert_status()
    # get the current version
    old_version = get_version()
    if major is True and all([x is False for x in [minor, patch]]):
        new_version = semver.bump_major(old_version)
    elif minor is True and all([x is False for x in [major, patch]]):
        new_version = semver.bump_minor(old_version)
    elif patch is True and all([x is False for x in [major, minor]]):
        new_version = semver.bump_patch(old_version)
    else:
        raise RuntimeError("Can only update one of major, minor, or patch")
    is_python = is_python_package()
    is_node = is_node_package()
    if is_python and not is_node:
        return bump_version_python(old_version, new_version)
    elif is_node and not is_python:
        return bump_version_node(old_version, new_version)
    elif is_python and is_node:
        raise RuntimeError("Both python and node packages were detected.")
    else:
        raise RuntimeError("No python or node package was detected.")

