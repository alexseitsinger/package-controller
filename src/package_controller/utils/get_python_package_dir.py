import os

from .find_file import find_file


def get_python_package_dir():
    # Find the root dir for the package.
    setup_file = find_file("setup.py")
    # get the package root directory
    root_dir = os.path.dirname(os.path.abspath(setup_file))
    # get the package name from the root dir.
    directory_name = os.path.basename(root_dir)
    # Find the package source directory
    src_dir = os.path.join(root_dir, "src")
    # get the package directory.
    if os.path.isdir(src_dir):
        package_dir = os.path.join(src_dir, directory_name)
        if not os.path.isdir(package_dir):
            package_name = directory_name.replace("-", "_")
            package_dir = os.path.join(src_dir, package_name)
    else:
        package_dir = os.path.join(root_dir, directory_name)
        if not os.path.isdir(package_dir):
            package_name = directory_name.replace("-", "_")
            package_dir = os.path.join(root_dir, package_name)
    # convert the directory name to a python-allowed package name.
    if not os.path.isdir(package_dir):
        raise NotADirectoryError(
            "The package directory does not exist. ({})".format(package_dir))
    # Return the path to the package dir.
    return package_dir

