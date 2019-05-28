from .git_add import git_add
from .git_commit import git_commit
from .git_tag import git_tag
from .make_changelog import make_changelog
from .find_init_module import find_init_module
from .run import run
from .is_python_package import is_python_package


def git_update(old_version, new_version):
    # save the last commit hash in case we need to reset.
    last_commit_hash = run("git", "rev-parse", "HEAD") 
    
    # create and add the changelog and init module.
    git_add(make_changelog())

    if is_python_package():
        git_add(find_init_module())
    
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
