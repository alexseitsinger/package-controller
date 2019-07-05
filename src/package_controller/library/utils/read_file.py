import re
import json
from io import open


RE_VARIABLE = r"^{} = ['\"]([^'\"]*)['\"]"


def read_file(path, variable=None):
    with open(path, "r") as f:
        content = f.read()
        if path.endswith(".py"):
            if variable is None:
                return content
            regex = RE_VARIABLE.format(variable)
            match = re.search(regex, content, re.M)
            if match:
                return match.group(1)
            raise AttributeError("{} was not found in {}".format(variable, path))
        elif path.endswith(".json"):
            data = json.loads(content)
            if variable is None:
                return data
            return data[variable]
        else:
            return content
