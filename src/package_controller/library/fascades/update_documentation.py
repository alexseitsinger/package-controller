import os

from ..python.is_python_package import is_python_package
from ..node.is_node_package import is_node_package
from ..generic.assert_which import assert_which
from ..node.create_readme import create_readme
from ..node.find_index_file import find_index_file
from ..generic.assert_readme_content import assert_readme_content

README_NAME = "README.md"


def update_documentation_node():
    assert_which("documentation")
    root_dir = os.getcwd()
    index_file = find_index_file(root_dir)
    readme_file = create_readme(index_file, README_NAME)
    try:
        assert_readme_content(readme_file)
    except AssertionError:
        print("Creating {} from entire src directory.".format(README_NAME))
        readme_file = create_readme("src/**", README_NAME)
    return readme_file


def update_documentation_python():
    pass


def update_documentation():
    is_python = is_python_package()
    is_node = is_node_package()
    if is_python and not is_node:
        return update_documentation_python()
    elif is_node and not is_python:
        return update_documentation_node()
    elif is_node and is_python:
        raise RuntimeError("Both python and node packages were detected.")
    else:
        raise RuntimeError("No python or node package was detected.")
