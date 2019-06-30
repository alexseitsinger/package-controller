import os

from ..find_file import find_file
from .get_python_package_dir import get_python_package_dir


def find_init_module():
    # In the package source root, find the init module.
    package_dir = get_python_package_dir()
    init_module = os.path.join(package_dir, "__init__.py")
    if not os.path.exists(init_module):
        raise FileNotFoundError(
            "The init module does not exist. ({})".format(init_module)
        )
    return init_module
