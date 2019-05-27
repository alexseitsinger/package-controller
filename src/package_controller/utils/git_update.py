from .git_add import git_add
from .git_commit import git_commit
from .git_tag import git_tag
from .make_changelog import make_changelog
from .find_init_module import find_init_module
from .run import run


def git_update(current_version, next_version):
    # save the last commit hash in case we need to reset.
    last_commit_hash = run("git", "rev-parse", "HEAD")

    # Create the release commit.
    init_module = find_init_module()
    changelog = make_changelog()
    git_add(init_module, changelog)
    commit_hash = git_commit(
        commit_type="chore",
        subject=next_version,
        description="Updates the version from {} to {}".format(
            current_version, next_version
        )
    )

    # Create a new tag pointing to this commit.
    try:
        tag_name = "v{}".format(next_version)
        git_tag(tag_name, commit_hash)
    except RuntimeError as exc:
        run("git", "reset", "--hard", last_commit_hash)
        raise exc
