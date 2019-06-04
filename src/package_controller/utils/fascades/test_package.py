import os

from ..generic.assert_which import assert_which
from ..generic.find_file import find_file
from ..generic.run import run
from ..node.is_node_package import is_node_package
from ..python.is_python_package import is_python_package


def test_package_node():
    assert_which("node")
    try:
        assert_which("yarn")
        return run("yarn run test")
    except AssertionError:
        assert_which("npm")
        return run("npm run test")


def test_package_python(unit, integration):
    # Make sure our required programs are installed.
    assert_which("python")
    assert_which("pipenv")
    assert_which("pytest")

    # Find the dirs to navigate into.
    setup_file = find_file("setup.py")
    root = os.path.dirname(setup_file)
    src_dir = os.path.join(root, "src")
    tests_dir = os.path.join(src_dir, "tests")
    for dir_path in [src_dir, tests_dir]:
        if not os.path.isdir(dir_path):
            raise NotADirectoryError("Directory does not exist. ({})".format(dir_path))

    # Run the test suites, and save their outputs.
    unit_tests_output = None
    if unit is True:
        unit_tests_dir = os.path.join(tests_dir, "unit")
        if not os.path.isdir(unit_tests_dir):
            raise NotADirectoryError("Unit tests directory does not exist. ({})".format(unit_tests_dir))
        unit_tests_output = run("pipenv run pytest {}".format(unit_tests_dir), raise_exception=False)

    integration_tests_output = None
    if integration is True:
        integration_tests_dir = os.path.join(tests_dir, "integration")
        if not os.path.isdir(integration_tests_dir):
            raise NotADirectoryError("Integration tests directory does not exist. ({})".format(integration_tests_dir))
        integration_tests_output = run("pipenv run pytest {}".format(integration_tests_dir), raise_exception=False)

    # Return the outputs for console messages.
    return (unit_tests_output, integration_tests_output,)


def test_package(unit, integration):
    # Raise an exception if not tests are sselected.
    if unit is False and integration is False:
        raise RuntimeError("No unit or integration tests were chosen.")

    # Run the correct method based on the package language.
    is_python = is_python_package()
    is_node = is_node_package()
    if is_python and not is_node:
        return test_package_python(unit, integration)
    elif is_node and not is_python:
        return test_package_node(unit, integration)
    elif is_python and is_node:
        raise RuntimeError("Both python and node packages were detected.")
    else:
        raise RuntimeError("No python or node package was detected.")
