import os

from .get_version import get_version
from .find_file import find_file
from .run import run

TWINE_UPLOAD_ARGS = ["twine", "upload"]
TARBALL_NAME = "{}-{}.tar.gz"
WHEEL_NAME = "{}-{}-py3-none-any.whl"


def twine_upload():
    version = get_version()
    setup_module = find_file("setup.py")
    root = os.path.dirname(setup_module)
    name = os.path.basename(root)
    dist_dir = os.path.join(root, "dist")
    wheel_name = WHEEL_NAME.format(name, version)
    wheel = os.path.join(dist_dir, wheel_name)
    tarball_name = TARBALL_NAME.format(name, version)
    tarball = os.path.join(dist_dir, tarball_name)
    # Check if the wheel exists.
    if not os.path.exists(wheel):
        raise RuntimeError("Wheel does not exist. ({})".format(wheel))
    # Check if the tarball exists.
    if not os.path.exists(tarball):
        raise RuntimeError("Tarball does not exist. ({})".format(tarball))
    # Upload the files to pypi.
    twine_upload_args = TWINE_UPLOAD_ARGS + [wheel, tarball]
    out = run(*twine_upload_args)
    return out
