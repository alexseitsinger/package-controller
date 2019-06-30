import json

from ..utils.assert_which import assert_which
from ..utils.find_file import find_file
from ..utils.run import run
from ..utils.git.push import push
from ..utils.node.is_node_package import is_node_package
from ..utils.python.is_python_package import is_python_package
from ..utils.python.twine_upload import twine_upload


YARN_PUBLISH_COMMAND = "yarn publish --non-interactive --access {} --new-version {}"


def get_yarn_publish_command(new_version, access="public", otp=None):
    cmd = YARN_PUBLISH_COMMAND.format(access, new_version)
    if otp is not None:
        cmd = " ".join([cmd, "--otp {}".format(otp)])
    return cmd


def get_npm_publish_command(new_version, access="public", otp=None):
    return ""


def publish_node(access="public", otp=None):
    assert_which("node")
    package_file = find_file("package.json")
    package_name = None
    package_version = None
    with open(package_file, "r") as f:
        package_file_json = json.loads(f.read())
        package_name = package_file_json["name"]
        package_version = package_file_json["version"]
    try:
        assert_which("yarn")
        cmd = get_yarn_publish_command(package_version, access, otp)
    except AssertionError:
        assert_which("npm")
        cmd = get_npm_publish_command(package_version, access, otp)
    run(cmd)
    return [package_name]


def publish_python():
    assert_which("python")
    return twine_upload()


def publish(access="public", otp=None):
    is_python = is_python_package()
    is_node = is_node_package()
    if is_python and not is_node:
        return publish_python()
    elif is_node and not is_python:
        return publish_node(access, otp)
    elif is_python and is_node:
        raise RuntimeError("Both python and node packages detected.")
    else:
        raise RuntimeError("No python or node package was detected.")
