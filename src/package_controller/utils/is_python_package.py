from .find_file import find_file


def is_python_package():
    try:
        find_file("setup.py")
        return True
    except RuntimeError as exc:
        return False
