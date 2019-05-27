import os

from .find_file import find_file


def find_init_module():
    # Find the root dir for the package.
    setup_file = find_file("setup.py")
    # get the package root directory
    root_dir = os.path.dirname(os.path.abspath(setup_file))
    # get the package name from the root dir.
    directory_name = os.path.basename(root_dir)
    # convert the directory name to a python-allowed package name.
    package_name = directory_name.replace("-", "_")
    # Find the package source directory
    src_dir = os.path.join(root_dir, "src")
    if os.path.exists(src_dir):
        package_dir = os.path.join(src_dir, package_name)
    else:
        package_dir = os.path.join(root_dir, package_name)
    if not os.path.exists(package_dir):
        raise RuntimeError("The package directory does not exist. ({})".format(
                           package_dir))
    # In the package source root, find the init module.
    init_module = os.path.join(package_dir, "__init__.py")
    if not os.path.exists(init_module):
        raise RuntimeError("The init module does not exist. ({})".format(
                           init_module))
    return init_module

