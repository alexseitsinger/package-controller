import re

from ..pipe_commands import pipe_commands


def get_python_package_version(name):
    output = pipe_commands(["pipenv graph", "grep {}".format(name)])
    try:
        if output.startswith("  - "):
            pattern = r"installed: ([\d.]+)"
            m = re.search(pattern, output)
            version = m.groups()[0]
        else:
            bits = output.split("==")
            version = bits[1]
        return version.strip()
    except IndexError:
        raise RuntimeError("Failed to get python package version. ({})".format(name))
