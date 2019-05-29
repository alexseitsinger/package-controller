import os
import json

from .run import run
from .get_version import get_version
from .find_file import find_file
from .assert_status import assert_status
from .assert_which import assert_which
from .is_python_package import is_python_package
from .is_node_package import is_node_package


BUILD_ARGS = ["python", "setup.py", "sdist", "bdist_wheel"]
PIPENV_RUN_ARGS = ["pipenv", "run"]
TARBALL_NAME = "{}-{}.tar.gz"
WHEEL_NAME = "{}-{}-py3-none-any.whl"
YARN_RUN_BUILD_ARGS = ["yarn", "run", "build"]
NPM_RUN_BUILD_ARGS = ["npm", "run", "build"]


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
            raise RuntimeError("File already exists. ({})".format(path))
    try:
        assert_which("pipenv")
        run(*PIPENV_RUN_ARGS + BUILD_ARGS)
        return built
    # add check for exception message to ensure we either:
    # 1. attempt the command with pipenv or another manager.
    # 2. raise the exception since its something else.
    except RuntimeError as exc:
        msg = str(exc)
        if msg == "Executable was not found. (pipenv)":
            run(*BUILD_ARGS)
            return built
        raise RuntimeError("Failed to build python package using pipenv and python.")


def build_package_node():
    assert_which("node")
    package_file = find_file("package.json")
    built = []
    with open(package_file, "r") as f:
        package_file_json = json.loads(f.read())
        built +=  [package_file_json["name"]]
    try:
        assert_which("yarn")
        run(*YARN_RUN_BUILD_ARGS)
        return built
    except RuntimeError as exc:
        msg = str(exc)
        if msg == "Executable was not found. (yarn)":
            assert_which("npm")
            run(*NPM_RUN_BUILD_ARGS)
            return built
        raise RuntimeError("Neither Yarn or NPM were found.")


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

