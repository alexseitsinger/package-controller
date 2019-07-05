"""
https://developer.github.com/v3/repos/#create
"""

import json
import requests

from .get_authorized_session import get_authorized_session


def create_personal_repository(
    username,
    name,
    description,
    homepage,
    private=False,
    has_issues=True,
    has_projects=True,
    has_wiki=True,
    auto_init=False,
    gitignore_template=None,
    license_template="bsd-2-clause",
    allow_squash_merge=False,
    allow_merge_commit=False,
    allow_rebase_merge=False,
    timeout=5.0,
):
    try:
        url = "https://api.github.com/user/repos"
        session = get_authorized_session(username)
        response = session.post(
            url,
            data=json.dumps(
                {
                    "name": name,
                    "description": description,
                    "homepage": homepage,
                    "private": private,
                    "has_issues": has_issues,
                    "has_projects": has_projects,
                    "has_wiki": has_wiki,
                    "auto_init": auto_init,
                    "gitignore_template": gitignore_template,
                    "license_template": license_template,
                    "allow_squash_merge": allow_squash_merge,
                    "allow_merge_commit": allow_merge_commit,
                    "allow_rebase_merge": allow_rebase_merge,
                }
            ),
            timeout=timeout,
        )
        if not str(response.status_code).startswith("2"):
            raise RuntimeError(
                "Failed to create personal repository.\n\n{}\n\n{}: {}".format(
                    url, response.status_code, response.text
                )
            )
        return response.json()
    except requests.ConnectionError:
        raise requests.ConnectionError(
            "Failed to connect to {} within {} seconds.".format(url, timeout)
        )
