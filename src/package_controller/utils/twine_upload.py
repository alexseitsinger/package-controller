import os

from .get_version import get_version
from .find_file import find_file
from .run import run
from .assert_status import assert_status
from .assert_which import assert_which

TWINE_UPLOAD_ARGS = ["twine", "upload"]
TARBALL_NAME = "{}-{}.tar.gz"
WHEEL_NAME = "{}-{}-py3-none-any.whl"


def twine_upload():
    assert_status()
    version = get_version()
    setup_module = find_file("setup.py")
    root = os.path.dirname(setup_module)
    directory_name = os.path.basename(root)
    package_name = directory_name.replace("-", "_")
    dist_dir = os.path.join(root, "dist")
    wheel_name = WHEEL_NAME.format(package_name, version)
    wheel = os.path.join(dist_dir, wheel_name)
    tarball_name = TARBALL_NAME.format(package_name, version)
    tarball = os.path.join(dist_dir, tarball_name)
    uploaded = [wheel, tarball]
    for path in uploaded:
        if not os.path.exists(path):
            raise FileNotFoundError("File does not exist. ({})".format(path))
    # Check if Twine exists on PATH.
    assert_which("twine")
    # Run the command
    run(*TWINE_UPLOAD_ARGS + uploaded)
    # Return the list of paths we uploaded.
    return uploaded
