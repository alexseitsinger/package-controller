from .git_add import git_add
from .git_commit import git_commit
from .git_tag import git_tag
from .make_changelog import make_changelog
from .find_init_module import find_init_module


def git_update(current_version, next_version):
    # Get the init module that the version is saved to.
    init_module = find_init_module()
    # Add it to git.
    git_add(init_module)
    # Commit the change, and get the new hash.
    commit_hash = git_commit(
        type="docs",
        subject="updates the version",
        description="updates the version from {} to {}".format(
            current_version, next_version
        ),
    )
    # Create a new tag pointing to this commit.
    tag_name = "v{}".format(next_version)
    git_tag(name=tag_name, hash=commit_hash)
    # Try to create the changelog.
    changelog = make_changelog()
    git_add(changelog)
    git_commit(
        type="docs",
        subject="updates the changelog".format(tag_name),
        description="updates the changelog for {}".format(tag_name),
    )

