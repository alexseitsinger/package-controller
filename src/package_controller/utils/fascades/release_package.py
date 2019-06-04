import json

from ..generic.assert_which import assert_which
from ..generic.find_file import find_file
from ..generic.run import run
from ..git.push import push
from ..node.is_node_package import is_node_package
from ..python.is_python_package import is_python_package
from ..python.twine_upload import twine_upload


def release_package_node():
    assert_which("node")
    # get the package info
    package_file = find_file("package.json")
    package_name = None
    with open(package_file, "r") as f:
        package_file_json = json.loads(f.read())
        package_name = package_file_json["name"]
    try:
        assert_which("yarn")
        run("yarn publish --access public")
    except AssertionError:
        assert_which("npm")
        run("npm publish --access public")
    return [package_name]


def release_package_python():
    assert_which("python")
    return twine_upload()


def release_package(remote="origin", branch="master", tag_name=None):
    is_python = is_python_package()
    is_node = is_node_package()
    push(remote=remote, branch=branch, tag_name=tag_name)
    if is_python and not is_node:
        return release_package_python()
    elif is_node and not is_python:
        return release_package_node()
    elif is_python and is_node:
        raise RuntimeError("Both python and node packages detected.")
    else:
        raise RuntimeError("No python or node package was detected.")
