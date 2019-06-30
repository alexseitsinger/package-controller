import re
from io import open

RE_VARIABLE = r"^{} = ['\"]([^'\"]*)['\"]"


def read_file(path, variable=None):
    with open(path, "r") as f:
        content = f.read()
        if variable is None:
            return content
        regex = RE_VARIABLE.format(variable)
        match = re.search(regex, content, re.M)
        if match:
            return match.group(1)
        raise AttributeError("{} does not exist in {}".format(variable, path))
