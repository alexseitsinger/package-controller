import os
import json

from ..get_config_file import get_config_file


def get_personal_access_token(username):
    token = os.environ.get("GITHUB_PERSONAL_ACCESS_TOKEN", None)
    if token is None:
        config_file = get_config_file()
        # Read the cred file for our remote url.
        with open(config_file, "r") as fr:
            data = json.loads(fr.read())
            try:
                tokens = data["tokens"]
            except AttributeError:
                tokens = data["tokens"] = {}
                with open(config_file, "w") as fw:
                    fw.write(json.dumps(data))
            try:
                token = tokens[username]
            except AttributeError:
                raise AttributeError(
                    "The username ({}) has no personal access token saved.".format(
                        username
                    )
                )
    if token is None:
        raise RuntimeError(
            "Failed to find a personal access token for {}.".format(username)
        )
    return token
