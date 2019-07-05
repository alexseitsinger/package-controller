import json

from get_config_file import get_config_file
from .read_file import read_file


def get_config_settings(language=None):
    # Get the config file path from the filesystem.
    config_file = get_config_file()
    # Read the settings variable from the config file.
    with open(config_file, "r") as fr:
        content = json.loads(fr.read())
        try:
            settings = content["settings"]
        except AttributeError:
            settings = content["settings"] = {}
    # If no language specified, return all settings.
    if language is None:
        return settings
    # If language settings exist, return them.
    try:
        return settings[language]
    except AttributeError:
        settings[language] = {
            "root": "",
            "templates": "",
            "library": {"active": "", "deprecated": ""},
        }
        with open(config_file, "w") as fw:
            fw.write(json.dumps(content))
        return settings[language]
