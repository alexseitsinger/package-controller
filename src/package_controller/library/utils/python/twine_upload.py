import os

from ...commands.version import version
from ..assert_which import assert_which
from ..find_file import find_file
from ..run import run
from ..git.assert_status import assert_status


TWINE_UPLOAD_ARGS = ["twine", "upload"]
TARBALL_NAME = "{}-{}.tar.gz"
WHEEL_NAME = "{}-{}-py3-none-any.whl"


def twine_upload():
    assert_status()
    current_version = version()
    setup_module = find_file("setup.py")
    root = os.path.dirname(setup_module)
    directory_name = os.path.basename(root)
    dist_dir = os.path.join(root, "dist")
    if not os.path.isdir(dist_dir):
        raise NotADirectoryError("Dist directory does not exist.")
    package_names = [directory_name, directory_name.replace("-", "_")]
    wheel_names = [WHEEL_NAME.format(x, current_version) for x in package_names]
    tarball_names = [TARBALL_NAME.format(x, current_version) for x in package_names]
    wheel = None
    for wheel_name in wheel_names:
        if wheel is None:
            wheel_path = os.path.join(dist_dir, wheel_name)
            if os.path.exists(wheel_path):
                wheel = wheel_path
    tarball = None
    for tarball_name in tarball_names:
        if tarball is None:
            tarball_path = os.path.join(dist_dir, tarball_name)
            if os.path.exists(tarball_path):
                tarball = tarball_path
    built = [wheel, tarball]
    for built_file in built:
        if built_file is None or not os.path.exists(built_file):
            raise FileNotFoundError("File does not exist. ({})".format(built_file))
    # Check if Twine exists on PATH.
    assert_which("twine")
    # Run the command
    run("twine upload {}".format(" ".join(built)))
    # Return the list of paths we uploaded.
    return built
