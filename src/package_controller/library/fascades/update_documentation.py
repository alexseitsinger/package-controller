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
    # Find the package's index file, or raise an exception.
    index_file = find_index_file(root_dir)
    # Attempt to create the README from the index file first.
    readme_file = create_readme(root_dir, index_file, README_NAME)
    # Check if the created README is empty...
    try:
        assert_readme_content(readme_file)
    except AssertionError:
        # If it is empty, attempt to create another README from the src
        # directory instead of just the index file.
        print("Creating {} from entire src directory.".format(README_NAME))
        readme_file = create_readme(root_dir, "src/**", README_NAME)
        # If it's still empty, raise another exception.
        assert_readme_content(readme_file)
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
