import os

from .run import run
from .get_version import get_version
from .find_file import find_file

BUILD_ARGS = ["python", "setup.py", "sdist", "bdist_wheel"]
PIPENV_RUN_ARGS = ["pipenv", "run"]
TARBALL_NAME = "{}-{}.tar.gz"
WHEEL_NAME = "{}-{}-py3-none-any.whl"


def build_package():
    current_version = get_version()
    setup_file = find_file("setup.py")
    root = os.path.dirname(setup_file)
    name = os.path.basename(root)
    dist_dir = os.path.join(root, "dist")
    wheel_name = WHEEL_NAME.format(name, current_version)
    wheel = os.path.join(dist_dir, wheel_name)
    tarball_name = TARBALL_NAME.format(name, current_version)
    tarball = os.path.join(dist_dir, tarball_name)
    if os.path.exists(wheel):
        raise RuntimeError("Wheel already exists. ({})".format(
            os.path.basename(wheel)
        ))
    if os.path.exists(tarball):
        raise RuntimeError("Tarball already exists. ({})".format(
            os.path.basename(tarball)
        ))
    try:
        return run(*BUILD_ARGS)
    except RuntimeError:
        args = PIPENV_RUN_ARGS + BUILD_ARGS
        return run(*args)

