from .git_add import git_add
from .git_commit import git_commit
from .git_tag import git_tag
from .assert_status import assert_status
from .make_changelog import make_changelog
from .find_init_module import find_init_module
from .run import run
from .is_python_package import is_python_package
from .is_node_package import is_node_package
from .find_file import find_file


def git_update_node(old_version, new_version):
    # We dont need to do anything here since its done automatically by yarn.
    # when we run `pc version`
    return (None, None)


def git_update_python(old_version, new_version):
    # save the last commit hash in case we need to reset.
    last_commit_hash = run("git", "rev-parse", "HEAD") 
    
    # create and add the changelog and init module..
    git_add(make_changelog(), find_init_module())
    
    # create the new commit.
    commit_hash = git_commit(
        commit_type="chore",
        subject=new_version,
        description="Updates the version from {} to {}".format(
            old_version, new_version
        )
    )

    # Create a new tag pointing to this commit.
    try:
        tag_name = "v{}".format(new_version)
        return git_tag(tag_name, commit_hash)
    except RuntimeError as exc:
        run("git", "reset", "--hard", last_commit_hash)
        raise exc


def git_update(old_version, new_version):
    is_python = is_python_package()
    is_node = is_node_package()
    if is_python and not is_node:
        return git_update_python(old_version, new_version)
    elif is_node and not is_python:
        return git_update_node(old_version, new_version)
    elif is_node and is_python:
        raise RuntimeError("Both python and node packages were detected.")
    else:
        raise RuntimeError("No python or node package was detected.")

