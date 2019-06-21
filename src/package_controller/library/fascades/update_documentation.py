import os

from .get_version import get_version
from ..python.is_python_package import is_python_package
from ..node.is_node_package import is_node_package
from ..generic.assert_which import assert_which
from ..generic.run import run
from ..git.add import add
from ..git.commit import commit
from ..git.assert_status import assert_status

README_NAME = "README.md"


def update_documentation_node():
    assert_which("documentation")
    # Find the index file from the current directory.
    index_files = [
        os.path.join(os.getcwd(), "index.js"),
        os.path.join(os.getcwd(), "src/index.js"),
    ]
    index_file = None
    for f in index_files:
        if index_file is not None:
            continue
        if os.path.isfile(f):
            index_file = f
    # If the index file isn't found, raise an exception.
    if index_file is None:
        raise RuntimeError("Couldn't find index file for documentation.")
    # Create the relative path for the index file.
    index_file_rel_path = os.path.relpath(index_file, os.getcwd())
    # Create the documentation using the index file found.
    run("documentation build {} -f md -o {}".format(index_file_rel_path, README_NAME))
    try:
        assert_status()
    except AssertionError:
        add(README_NAME)
        current_version = get_version()
        commit(
            commit_type="docs",
            subject="Updates documentation for {}.".format(current_version),
        )
    return README_NAME


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
