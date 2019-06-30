import os


def find_index_file(root_dir):
    paths = [os.path.join(root_dir, "index.js"), os.path.join(root_dir, "src/index.js")]
    index_file = None
    for f in paths:
        if index_file is not None:
            continue
        if os.path.isfile(f):
            index_file = f
    if index_file is None:
        raise RuntimeError("Could not find the index file.")
    return index_file
