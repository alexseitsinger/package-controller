import click
import semver

from ..utils import (
    get_version,
    save_file,
    find_init_module,
    git_update,
)
from ..settings import DEFAULT_VERSION_VARIABLE


@click.command()
@click.option(
    "--variable",
    default=DEFAULT_VERSION_VARIABLE,
    required=False,
    help="The version variable in the file.")
@click.option("--patch", default=False, required=False, is_flag=True, help="Updates the patch version.")
@click.option("--minor", default=False, required=False, is_flag=True, help="Updates the minor version.")
@click.option("--major", default=False, required=False, is_flag=True, help="Updates the major version.")
@click.option("--git", default=False, required=False, is_flag=True, help="Updates git with new tag and changelog for version.")
def version(major, minor, patch, variable, git):
    current_version = get_version(variable=variable)
    init_module = find_init_module()
    if any([x is True for x in [major, minor, patch]]):
        if major is True and all([x is False for x in [minor, patch]]):
            next_version = semver.bump_major(current_version)
            save_file(init_module, variable, next_version)
            if git is True:
                git_update(
                    init_module=init_module,
                    current_version=current_version,
                    next_version=next_version
                )
            click.secho(
                "Successfully updated major version from {} to {}".format(
                    current_version, next_version
                ),
                fg="green"
            )
        elif minor is True and all([x is False for x in [major, patch]]):
            next_version = semver.bump_minor(current_version)
            save_file(init_module, variable, next_version)
            if git is True:
                git_update(
                    init_module=init_module,
                    current_version=current_version,
                    next_version=next_version
                )
            click.secho(
                "Successfully updated minor version from {} to {}".format(
                    current_version, next_version
                ),
                fg="green"
            )
        elif patch is True and all([x is False for x in [major, minor]]):
            next_version = semver.bump_patch(current_version)
            save_file(init_module, variable, next_version)
            if git is True:
                git_update(
                    init_module=init_module,
                    current_version=current_version,
                    next_version=next_version
                )
            click.secho(
                "Successfully updated patch version from {} to {}".format(
                    current_version, next_version
                ),
                fg="green"
            )
        else:
            click.secho(
                "Can only update one version: major, minor, or patch",
                fg="red"
            )
    else:
        click.secho(
            "Current version: {}".format(current_version),
            fg="yellow",
        )
