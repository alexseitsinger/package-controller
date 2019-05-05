import re

from ..exceptions import ReadFileException


def read_file(path, variable=None):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        if variable is None:
            return content
        regex = r"^{} = ['\"]([^'\"]*)['\"]".format(variable)
        match = re.search(regex, content, re.M)
        if match:
            return match.group(1)
        raise ReadFileException(
            "Unable to read variable ({}) in file ({})".format(variable, path)
        )


