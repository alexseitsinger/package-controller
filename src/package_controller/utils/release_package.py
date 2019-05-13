import os

from .run import run
from .find_file import find_file
from .get_version import get_version


GIT_PUSH_ARGS = ["git", "push" "origin", "master"]
GIT_PUSH_TAGS_ARGS = ["git", "push", "--tags"]
TWINE_UPLOAD_ARGS = ["twine", "upload"]
TARBALL_NAME = "{}-{}.tar.gz"
WHEEL_NAME = "{}-{}-py3-none-any.whl"


def release_package():
    version = get_version()
    setup_module = find_file("setup.py")
    root = os.path.dirname(setup_module)
    name = os.path.basename(root)
    dist_dir = os.path.join(root, "dist")
    wheel_name = WHEEL_NAME.format(name, version)
    wheel = os.path.join(dist_dir, wheel_name)
    tarball_name = TARBALL_NAME.format(name, version)
    tarball = os.path.join(dist_dir, tarball_name)
    # Check if the wheel and tarball files exist.
    if not all([os.path.exists(x) for x in [wheel, tarball]]):
        raise RuntimeError("Wheel and/or tarball does not exist.")
    run(TWINE_UPLOAD_ARGS + [wheel, tarball])
    run(GIT_PUSH_ARGS)
    run(GIT_PUSH_TAGS_ARGS)


