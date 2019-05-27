import re
from io import open


RE_VARIABLE = r"^{} = ['\"]([^'\"]*)['\"]"

def read_file(path, variable=None):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        if variable is None:
            return content
        regex = RE_VARIABLE.format(variable)
        match = re.search(regex, content, re.M)
        if match:
            return match.group(1)
        raise RuntimeError("Failed to read file. ({})".format(path))


