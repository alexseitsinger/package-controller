import os


FILE_NAME = "package-controller.json"


def get_config_file():
    home_path = os.path.abspath(os.path.expanduser("~"))
    config_path = os.path.join(home_path, FILE_NAME)
    # If the cred file doesn't exist, create it.
    if not os.path.exists(config_path):
        with open(config_path, "w") as fw:
            fw.write("{}")
    return config_path
