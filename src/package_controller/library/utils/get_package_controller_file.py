import os


FILE_NAME = "package-controller.json"


def get_package_controller_file():
    home_path = os.path.abspath(os.path.expanduser("~"))
    package_controller_file = os.path.join(home_path, FILE_NAME)
    # If the cred file doesn't exist, create it.
    if not os.path.exists(package_controller_file):
        with open(package_controller_file, "w") as fw:
            fw.write("{}")
    return package_controller_file
