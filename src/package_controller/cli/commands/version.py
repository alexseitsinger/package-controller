import click
import semver

from ...utils.git_update import git_update
from ...utils.bump_version import bump_version
from ...utils.get_version import get_version


@click.command()
@click.option(
    "--major", default=False, required=False, is_flag=True,
    help="Updates the major version.")
@click.option(
    "--minor", default=False, required=False, is_flag=True,
    help="Updates the minor version.")
@click.option(
    "--patch", default=False, required=False, is_flag=True,
    help="Updates the patch version.")
@click.option(
    "--no-git", default=False, required=False, is_flag=True,
    help="Do not update git with a new tag and changelog for version.")
@click.option(
    "--force", default=False, required=False, is_flag=True,
    help="Force the version update even if there are uncommitted changes.")
def version(major, minor, patch, no_git, force):
    if any([x is True for x in [major, minor, patch]]):
        try:
            old_version, new_version = bump_version(
                major=major, minor=minor, patch=patch, force=force)
            message = "Successfully updated version from {} to {}".format(
                old_version, new_version)
            if no_git is False:
                git_update(old_version, new_version)
            click.secho(message, fg="green", bold=True)
        except RuntimeError as exc:
            message = str(exc)
            if message == "git-changelog is not installed.":
                click.secho("Skipped creating changelog.", fg="yellow", bold=True)
                click.secho(message, fg="yellow")
            else:
                click.secho("Failed to update version.", fg="red", bold=True)
                click.secho(message, fg="red")
    else:
        message = "Current version: {}".format(get_version())
        click.secho(message, fg="yellow", bold=True)
