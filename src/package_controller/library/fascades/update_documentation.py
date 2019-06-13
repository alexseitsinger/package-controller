import os

from .get_version import get_version
from ..python.is_python_package import is_python_package
from ..node.is_node_package import is_node_package
from ..generic.assert_which import assert_which
from ..generic.run import run
from ..git.add import add
from ..git.commit import commit

README_NAME = "README.md"


def update_documentation_node():
    assert_which("documentation")
    run("documentation build ./src/index.js -f md -o {}".format(README_NAME))
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
