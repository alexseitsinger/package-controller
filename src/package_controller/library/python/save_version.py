from ..generic.replace_line import replace_line
from .find_init_module import find_init_module

RE_VARIABLE = r"^{} = ['\"][^'\"]*['\"]"
VERSION_VARIABLE = "__version__"
VERSION_VARIABLE_COMMENTS = [
    "# Do not change this version manually.\n",
    "# Versioning is managed by package_controller.\n",
    "# To update the version run `pc version --patch | --minor | --major`\n",
]


def save_version(next_version, file_path=None):
    if file_path is None:
        file_path = find_init_module()
    pattern = RE_VARIABLE.format(VERSION_VARIABLE)
    replacement = "{} = \"{}\"".format(VERSION_VARIABLE, next_version)
    replace_line(file_path, pattern, replacement, VERSION_VARIABLE_COMMENTS)
