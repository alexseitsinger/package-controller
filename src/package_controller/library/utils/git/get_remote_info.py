from ..run import run


def get_remote_info(name="origin"):
    url = run("git remote get-url {}".format(name))
    bits = url.split(":", 1)
    suffix = bits[1]
    parts = suffix.split("/", 1)
    owner_name = parts[0]
    repo_name = parts[1].rsplit(".", 1)[0]
    return (owner_name, repo_name)
