import semver

from .version import version
from ..utils.assert_which import assert_which
from ..utils.run import run
from ..utils.node.is_node_package import is_node_package
from ..utils.python.save_version import save_version
from ..utils.python.is_python_package import is_python_package
from ..utils.git.assert_commit import assert_commit
from ..utils.git.assert_status import assert_status


def bump_python(old_version, new_version):
    assert_which("python")
    save_version(new_version)
    return (old_version, new_version)


def bump_node(old_version, new_version):
    assert_which("node")
    assert_which("yarn")

    # Check if the tag already exists on a non-exist commit.
    tag = "v{}".format(new_version)
    tagged_commit = run("git rev-list -n 1 {}".format(tag))
    if tagged_commit is not None:
        try:
            assert_commit(tagged_commit)
        except AssertionError:
            print("Deleting tag ({}) for non-existent commit.".format(tag))
            run("git tag -d {}".format(tag))

    # update the version.
    message = "chore: {}".format(new_version)
    run("yarn version --new-version {} --message '{}'".format(new_version, message))

    # return the version numbers.
    return (old_version, new_version)


def bump(major=False, minor=False, patch=False, force=False):
    if force is False:
        assert_status()
    # get the current version
    old_version = version()
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
        return bump_python(old_version, new_version)
    elif is_node and not is_python:
        return bump_node(old_version, new_version)
    elif is_python and is_node:
        raise RuntimeError("Both python and node packages were detected.")
    else:
        raise RuntimeError("No python or node package was detected.")
