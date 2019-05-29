import json

from .twine_upload import twine_upload
from .is_python_package import is_python_package
from .is_node_package import is_node_package
from .run import run
from .find_file import find_file


def release_package_node():
    package_file = find_file("package.json")
    package_name = None
    with open(package_file, "r") as f:
        package_file_json = json.loads(f.read())
        package_name = package_file_json["name"]
    run("yarn", "publish", "--access", "public")
    return [package_name]


def release_package_python():
    return twine_upload()


def release_package():
    is_python = is_python_package()
    is_node = is_node_package()
    if is_python and not is_node:
        return release_package_python()
    elif is_node and not is_python:
        return release_package_node()
    elif is_python and is_node:
        raise RuntimeError("Both python and node packages detected.")
    else:
        raise RuntimeError("No python or node package was detected.")
