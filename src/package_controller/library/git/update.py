from ..generic.run import run
from ..python.find_init_module import find_init_module
from ..python.is_python_package import is_python_package
from .add import add
from .commit import commit
from .tag import tag
from .assert_repository import assert_repository
from .make_changelog import make_changelog


def update(old_version, new_version):
    assert_repository()

    # Create a tag for the latest commit.
    tag_name = "v{}".format(new_version)

    # If it's python, we have to add a commit manually.
    if is_python_package():
        # save the last commit hash in case we need to reset.
        last_commit_hash = run("git rev-parse HEAD")

        # If it's a python package, we've updated this version variable.
        # Make sure to include it in the commit.
        add(find_init_module())

        # create the new commit.
        commit_hash = commit(
            "chore",
            "{new_version}. Updates the version from {old_version} to {new_version}.".format(
                new_version=new_version, old_version=old_version
            ),
        )

        # Create the tag.
        try:
            tag(tag_name, commit_hash)
        except RuntimeError as exc:
            run("git reset --hard {}".format(last_commit_hash))
            raise exc

    # Create and add the changelog and init module.
    add(make_changelog())
    commit("chore", "Updates the changelog for {}".format(tag_name))

    # return the tag name to use somewhere else.
    return tag_name
