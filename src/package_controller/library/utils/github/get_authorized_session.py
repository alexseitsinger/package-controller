import requests

from .get_personal_access_token import get_personal_access_token


def get_authorized_session(username, password=None):
    session = requests.Session()
    if password is None:
        token = get_personal_access_token(username)
        session.headers.update({"Authorization": "token {}".format(token)})
    else:
        session.auth = (username, password)
    return session
