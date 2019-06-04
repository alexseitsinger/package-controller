from .git_add import git_add
from .git_commit import git_commit
from .git_tag import git_tag
from .make_changelog import make_changelog
from .find_init_module import find_init_module
from .run import run
from .is_python_package import is_python_package
from .assert_git_repository import assert_git_repository


def git_update(old_version, new_version):
    assert_git_repository()

    # Create a tag for the latest commit.
    tag_name = "v{}".format(new_version)

    # If it's python, we have to add a commit manually.
    if is_python_package():
        # save the last commit hash in case we need to reset.
        last_commit_hash = run("git rev-parse HEAD")

        # If it's a python package, we've updated this version variable.
        # Make sure to include it in the commit.
        git_add(find_init_module())

        # create the new commit.
        commit_hash = git_commit(
            commit_type="chore",
            subject=new_version,
            description="Updates the version from {} to {}".format(
                old_version, new_version
            )
        )

        # Create the tag.
        try:
            git_tag(tag_name, commit_hash)
        except RuntimeError as exc:
            run("git reset --hard {}".format(last_commit_hash))
            raise exc

    # Create and add the changelog and init module.
    git_add(make_changelog())
    git_commit(
        commit_type="chore",
        subject="Updates the changelog for {}".format(tag_name)
    )

    # return the tag name to use somewhere else.
    return tag_name
