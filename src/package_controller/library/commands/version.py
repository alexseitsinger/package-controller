import os
import json

from ..utils.read_file import read_file
from ..utils.find_file import find_file
from ..utils.python.find_init_module import find_init_module
from ..utils.python.is_python_package import is_python_package
from ..utils.node.is_node_package import is_node_package


PYTHON_VERSION_VARIABLE = "__version__"


def version_python(file_path=None, variable=PYTHON_VERSION_VARIABLE):
    if file_path is None:
        file_path = find_init_module()
    return read_file(file_path, variable)


def version_node(file_path=None):
    if file_path is None:
        file_path = find_file("package.json")
    content = read_file(file_path)
    content_json = json.loads(content)
    return content_json["version"]


def version(file_path=None, variable=PYTHON_VERSION_VARIABLE):
    is_python = is_python_package()
    is_node = is_node_package()
    if is_python and not is_node:
        return version_python(file_path, variable)
    elif is_node and not is_python:
        return version_node(file_path)
    elif is_node and is_python:
        raise RuntimeError("Both python and node packages detected.")
    else:
        raise RuntimeError("No python or node package was detected.")
