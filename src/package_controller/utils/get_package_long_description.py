import os

from .read_file import read_file
from .find_file import find_file
from ..exceptions import GetPackageLongDescriptionException


def get_package_long_description(file_name="README.md"):
    setup_file = find_file("setup.py")
    if setup_file is None:
        raise GetPackageLongDescriptionException(
            "Could not find setup file.",
        )
    root_dir = os.path.dirname(setup_file)
    readme_file = os.path.join(root_dir, file_name)
    if not os.path.exists(readme_file):
        raise GetPackageLongDescriptionException(
            "Readme file does not exist. ({})".format(readme_file)
        )
    return read_file(readme_file)
