import os
import json

from .get_version import get_version
from ..generic.find_file import find_file
from ..generic.assert_which import assert_which
from ..generic.run import run
from ..git.assert_status import assert_status
from ..node.is_node_package import is_node_package
from ..python.is_python_package import is_python_package


TARBALL_NAME = "{}-{}.tar.gz"
WHEEL_NAME = "{}-{}-py3-none-any.whl"
BUILD_CMD = "python setup.py sdist bdist_wheel"


def build_package_python():
    assert_which("python")
    current_version = get_version()
    package_file = find_file("setup.py")
    root = os.path.dirname(package_file)
    name = os.path.basename(root)
    dist_dir = os.path.join(root, "dist")
    wheel_name = WHEEL_NAME.format(name, current_version)
    wheel = os.path.join(dist_dir, wheel_name)
    tarball_name = TARBALL_NAME.format(name, current_version)
    tarball = os.path.join(dist_dir, tarball_name)
    built = [wheel, tarball]
    for path in built:
        if os.path.exists(path):
            raise FileExistsError("File already exists. ({})".format(path))
    try:
        assert_which("pipenv")
        run("pipenv run {}".format(BUILD_CMD))
    except AssertionError:
        run(BUILD_CMD)
    return built


def build_package_node():
    assert_which("node")
    package_file = find_file("package.json")
    built = []
    with open(package_file, "r") as f:
        package_file_json = json.loads(f.read())
        package_name = package_file_json["name"]
        built += [package_name]
    try:
        assert_which("yarn")
        run("yarn run build")
    except AssertionError:
        assert_which("npm")
        run("npm run build")
    return built


def build_package(force=False):
    if force is False:
        assert_status()
    is_python = is_python_package()
    is_node = is_node_package()
    if is_python and not is_node:
        return build_package_python()
    elif is_node and not is_python:
        return build_package_node()
    elif is_python and is_node:
        raise RuntimeError("Both python and node packages were detected.")
    else:
        raise RuntimeError("No python or node package was detected.")
