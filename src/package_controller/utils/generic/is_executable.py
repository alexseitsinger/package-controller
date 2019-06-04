import os


def is_executable(fpath):
    return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

