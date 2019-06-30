import json
import requests

from ..github.get_personal_access_token import get_personal_access_token
from ..github.get_authenticated_session import get_authenticated_session


GITHUB_RELEASES_URL = "https://github.com/repos/{}/{}/releases"


def create_release(
    owner_name,
    repo_name,
    tag_name,
    body,
    target="master",
    name=None,
    draft=True,
    prerelease=False,
    timeout=10.0,
):
    if name is None:
        name = tag_name
    try:
        url = GITHUB_RELEASES_URL.format(owner_name, repo_name)
        response = get_authenticated_session(owner_name).post(
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
                    url, response.status_code, response.text
                )
            )
        return response.json()
    except requests.ConnectionError:
        raise RuntimeError(
            "Failed to connect to {} within {} seconds.".format(url, timeout)
        )
