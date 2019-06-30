import json
import requests

from .get_personal_access_token import get_personal_access_token
from .get_authorized_session import get_authorized_session


GITHUB_RELEASES_URL = "https://api.github.com/repos/{}/{}/releases"


def create_release(
    owner_name,
    repo_name,
    tag_name,
    body,
    target="master",
    name=None,
    draft=False,
    prerelease=False,
    timeout=10.0,
):
    if name is None:
        name = tag_name
    try:
        url = GITHUB_RELEASES_URL.format(owner_name, repo_name)
        response = get_authorized_session(owner_name).post(
            url,
            data=json.dumps(
                {
                    "tag_name": tag_name,
                    "name": name,
                    "target_commitish": target,
                    "body": body,
                    "draft": draft,
                    "prerelease": prerelease,
                }
            ),
            headers={"Content-Type": "application/json"},
            timeout=timeout,
        )
        if not str(response.status_code).startswith("2"):
            raise RuntimeError(
                "Failed to create release.\n\n{}\n\n{}: {}".format(
                    url, response.status_code
                )
            )
        return response.json()
    except requests.ConnectionError:
        raise RuntimeError(
            "Failed to connect to {} within {} seconds.".format(url, timeout)
        )
