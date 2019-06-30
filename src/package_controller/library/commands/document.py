import os

from ..utils.assert_which import assert_which
from ..utils.assert_readme_content import assert_readme_content
from ..utils.node.is_node_package import is_node_package
from ..utils.node.create_readme import create_readme
from ..utils.node.find_index_file import find_index_file
from ..utils.python.is_python_package import is_python_package
from ..utils.git.commit_readme_file import commit_readme_file

README_NAME = "README.md"


def document_node(status_message):
    assert_which("documentation")
    root_dir = os.getcwd()
    input_file = "src/**"
    # If there is no source directory, try to find an index file.
    if not os.path.isdir(os.path.join(root_dir, "src")):
        input_file = find_index_file(root_dir)
        # If there is no index file, raise an exception.
        if not os.path.isfile(input_file):
            raise FileNotFoundError("There is no src directory or index file.")
    # Attempt to create the README from the index file first.
    readme_file = create_readme(root_dir, input_file, README_NAME)
    # Check if the created README is empty...
    assert_readme_content(readme_file)
    # Commit the file to git.
    commit_readme_file(readme_file)
    # return the path to the readme file.
    return readme_file


def document_python():
    pass


def document(status_message):
    is_python = is_python_package()
    is_node = is_node_package()
    if is_python and not is_node:
        return document_python()
    elif is_node and not is_python:
        return document_node(status_message)
    elif is_node and is_python:
        raise RuntimeError("Both python and node packages were detected.")
    else:
        raise RuntimeError("No python or node package was detected.")
