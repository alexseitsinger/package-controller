import os


def find_file(file_name, current_dir=None, flat=False):
    if current_dir is None:
        current_dir = os.getcwd()
    file_list = os.listdir(current_dir)
    parent_dir = os.path.dirname(current_dir)
    if file_name in file_list:
        return os.path.join(current_dir, file_name)
    elif flat is True or current_dir == parent_dir:
        raise FileNotFoundError("Failed to find {}".format(file_name))
    else:
        return find_file(file_name, parent_dir)
