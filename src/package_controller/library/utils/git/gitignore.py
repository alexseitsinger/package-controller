import requests
import os


GITHUB_URL = "https://raw.githubusercontent.com/github/gitignore/{}.gitignore"


def get_gitignore_for_language(language, timeout=5.0):
    try:
        language = language.capitalize()
        url = GITHUB_URL.format(language)
        response = requests.get(url, timeout=timeout)
        if not str(response.status_code).startswith("2"):
            raise requests.HTTPError(
                "Failed to get gitignore for {}.\n\n{}\n\n{}: {}".format(
                    language, url, response.status_code, response.text
                )
            )
        return response.text
    except requests.Timeout:
        raise requests.Timeout(
            "Failed to connect to {} within {} seconds.".format(url, timeout)
        )


def set_gitignore_for_language(language, replace=False):
    path = os.path.join(os.getcwd(), ".gitignore")
    if os.path.isfile(path):
        if replace is False:
            raise FileExistsError("There is already a .gitignore file.")
        print("Removing existing .gitignore.")
        os.remove(path)
    with open(path, "w") as f:
        f.write(get_gitignore_for_language(language))
    return path
