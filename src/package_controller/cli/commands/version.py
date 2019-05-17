import click
import semver

from ...utils import (
    git_update,
    bump_version,
    get_version,
)


@click.command()
@click.option("--major", default=False, required=False, is_flag=True, help="Updates the major version.")
@click.option("--minor", default=False, required=False, is_flag=True, help="Updates the minor version.")
@click.option("--patch", default=False, required=False, is_flag=True, help="Updates the patch version.")
@click.option("--git", default=True, required=False, is_flag=True, help="Updates git with new tag and changelog for version.")
def version(major, minor, patch, git):
    if any([x is True for x in [major, minor, patch]]):
        try:
            old_version, new_version = bump_version(major, minor, patch)
            message = "Successfully updated version from {} to {}".format(
                old_version, new_version
            )
            if git is True:
                git_update(old_version, new_version)
            click.secho(message, fg="green", bold=True)
        except RuntimeError as exc:
            click.secho("Failed to update version.", fg="red", bold=True)
            click.secho(str(exc), fg="red")
    else:
        message = "Current version: {}".format(get_version())
        click.secho(message, fg="yellow", bold=True)
