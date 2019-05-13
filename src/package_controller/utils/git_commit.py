from .run import run


GIT_COMMIT_ARGS = ["git", "commit"]
GIT_LAST_COMMIT_HASH_ARGS = ["git", "rev-parse", "HEAD"]

def git_commit(type, subject, description=None):
    header = "{type}: {subject}".format(type=type, subject=subject)
    commit_args = GIT_COMMIT_ARGS + ["-m", header]
    if description is not None:
        commit_args += ["-m", description]
    run(*commit_args)
    return run(*GIT_LAST_COMMIT_HASH_ARGS)

