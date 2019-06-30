import os
import json

from .version import version
from ..utils.run import run
from ..utils.git.push import push
from ..utils.git.get_latest_changelog import get_latest_changelog
from ..utils.git.get_remote_info import get_remote_info
from ..utils.github.create_release import create_release


def release(
    remote_name="origin",
    branch_name="master",
    force=False,
    prerelease=False,
    draft=False,
):
    # Get the tag name if we're creating one.
    tag_name = "v{}".format(version())
    # Push our changes.
    push(remote_name, branch_name, tag_name, force)
    # Create a new release on GitHUb for the tag we just created.
    owner_name, repo_name = get_remote_info(remote_name)
    return create_release(
        owner_name=owner_name,
        repo_name=repo_name,
        tag_name=tag_name,
        body=get_latest_changelog(),
        target=branch_name,
        prerelease=prerelease,
        draft=draft,
    )
