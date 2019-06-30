from ..find_file import find_file


def is_node_package():
    try:
        find_file("package.json")
        return True
    except FileNotFoundError:
        return False
