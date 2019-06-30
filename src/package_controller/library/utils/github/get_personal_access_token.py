import os
import json

from ..get_package_controller_file import get_package_controller_file


def get_personal_access_token(username):
    token = os.environ.get("GITHUB_PERSONAL_ACCESS_TOKEN", None)
    if token is None:
        controller_file = get_package_controller_file()
        # Read the cred file for our remote url.
        with open(controller_file, "r") as fr:
            try:
                data = json.loads(fr.read())
                token = data[username]["personal_access_token"]
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
