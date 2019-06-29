import json

from ..generic.assert_which import assert_which
from ..generic.find_file import find_file
from ..generic.run import run
from ..git.push import push
from ..node.is_node_package import is_node_package
from ..python.is_python_package import is_python_package
from ..python.twine_upload import twine_upload


def release_package_node(otp=None):
    assert_which("node")
    # get the package info
    package_file = find_file("package.json")
    package_name = None
    package_version = None
    with open(package_file, "r") as f:
        package_file_json = json.loads(f.read())
        package_name = package_file_json["name"]
        package_version = package_file_json["version"]
    cmd = "yarn publish --non-interactive --access public --new-version {}".format(
        package_version
    )
    if otp is not None:
        cmd = "{} --otp {}".format(cmd, otp)
    run(cmd)
    return [package_name]


def release_package_python():
    assert_which("python")
    return twine_upload()


def release_package(
    remote="origin", branch="master", tag_name=None, otp=None, force=False
):
    is_python = is_python_package()
    is_node = is_node_package()
    push(remote=remote, branch=branch, tag_name=tag_name, force=force)
    if is_python and not is_node:
        return release_package_python()
    elif is_node and not is_python:
        return release_package_node(otp=otp)
    elif is_python and is_node:
        raise RuntimeError("Both python and node packages detected.")
    else:
        raise RuntimeError("No python or node package was detected.")
