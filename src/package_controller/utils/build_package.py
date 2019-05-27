import os

from .run import run
from .get_version import get_version
from .find_file import find_file
from .git_status import git_status
from .which import assert_which

BUILD_ARGS = ["python", "setup.py", "sdist", "bdist_wheel"]
PIPENV_RUN_ARGS = ["pipenv", "run"]
TARBALL_NAME = "{}-{}.tar.gz"
WHEEL_NAME = "{}-{}-py3-none-any.whl"


def build_package(force=False):
    if force is False:
        git_status()
    current_version = get_version()
    setup_file = find_file("setup.py")
    root = os.path.dirname(setup_file)
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
        run(*BUILD_ARGS)
        return built
    # add check for exception message to ensure we either:
    # 1. attempt the command with pipenv or another manager.
    # 2. raise the exception since its something else.
    except RuntimeError:
        assert_which("pipenv")
        run(*PIPENV_RUN_ARGS + BUILD_ARGS)
        return built

