import click
import semver

from ...utils import (
    get_version,
    save_version,
    git_update,
)

VERSION_NAMES = ("major", "minor", "patch",)
UPDATE_SUCCESS_MESSAGE = "Successfully updated {} version from {} to {}"
UPDATE_FAILURE_MESSAGE = "Can only update one version: {}, {}, or {}".format(*list(VERSION_NAMES))
UPDATE_STATUS_MESSAGE = "Current version: {}"

@click.command()
@click.option("--{}".format(VERSION_NAMES[0]), default=False, required=False, is_flag=True, help="Updates the {} version.".format(VERSION_NAMES[0]))
@click.option("--{}".format(VERSION_NAMES[1]), default=False, required=False, is_flag=True, help="Updates the {} version.".format(VERSION_NAMES[1]))
@click.option("--{}".format(VERSION_NAMES[2]), default=False, required=False, is_flag=True, help="Updates the {} version.".format(VERSION_NAMES[2]))
@click.option("--git", default=False, required=False, is_flag=True, help="Updates git with new tag and changelog for version.")
def version(major, minor, patch, git):
    current_version = get_version()
    next_version = None
    message = UPDATE_STATUS_MESSAGE.format(current_version)
    # If any of the flags are True, continue to create the next_version.
    # Otherwise, just print out the current version.
    if any([x is True for x in [major, minor, patch]]):
        if major is True and all([x is False for x in [minor, patch]]):
            next_version = semver.bump_major(current_version)
            message = UPDATE_SUCCESS_MESSAGE.format(VERSION_NAMES[0], current_version, next_version)
        elif minor is True and all([x is False for x in [major, patch]]):
            next_version = semver.bump_minor(current_version)
            message = UPDATE_SUCCESS_MESSAGE.format(VERSION_NAMES[1], current_version, next_version)
        elif patch is True and all([x is False for x in [major, minor]]):
            next_version = semver.bump_patch(current_version)
            message = UPDATE_SUCCESS_MESSAGE.format(VERSION_NAMES[2], current_version, next_version)
        else:
            message = UPDATE_FAILURE_MESSAGE
        # If we don't get a next_version, just print an error message.
        # Otherwise, save the next_version and update git (if flag is passed)
        if next_version is None:
            click.secho(message, fg="red")
        else:
            save_version(next_version)
            if git is True:
                git_update(current_version, next_version)
            click.secho(message, fg="green")
    else:
        click.secho(message, fg="yellow")
