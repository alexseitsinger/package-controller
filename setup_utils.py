import os
import re

ROOT = os.path.abspath(os.path.dirname(__file__))
PACKAGE_NAME = os.path.basename(ROOT)


def read(path, variable=None):
    file_path = os.path.join(ROOT, *path)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    if variable is None:
        return content
    regex = "{} = ['\"](^[^'\"]*)['\"]".format(variable)
    match = re.search(regex, content, re.M)
    if match:
        return match.group(1)
    raise RuntimeError(
        "Failed to read variable {} in file {}".format(
            variable, file_path,
        )
    )

