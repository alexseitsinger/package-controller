import requests

from .get_personal_access_token import get_personal_access_token


GITHUB_API_URL = "https://api.github.com/user"


def get_authenticated_session(username, password=None, timeout=10.0):
    session = requests.Session()
    if password is None:
        password = get_personal_access_token(username)
    session.auth = (username, password)
    try:
        response = session.post("https://api.github.com/user")
        if response.status_code != 200:
            raise RuntimeError(
                "Failed to authenticate session.\n\n{}: {}".format(
                    response.status_code, response.text
                )
            )
        return session
    except requests.ConnectionError:
        raise requests.RuntimeError(
            "Failed to connect to GitHub within {} seconds.".format(timeout)
        )
