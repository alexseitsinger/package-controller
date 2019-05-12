from .run import run


def git_commit(type, subject, description):
    header = "{type}: {subject}".format(type=type, subject=subject)
    run("git", "commit", "-m", header, "-m", description)
    return run("git", "rev-parse", "HEAD")

