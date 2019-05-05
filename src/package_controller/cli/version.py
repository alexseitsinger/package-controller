import click
import semver

from ..utils import (
    get_package_version,
    save_file,
    find_init_module,
)
from ..settings import DEFAULT_VERSION_VARIABLE


@click.command()
@click.option("--variable", default=DEFAULT_VERSION_VARIABLE, required=False)
@click.option("--patch", default=False, required=False, is_flag=True)
@click.option("--minor", default=False, required=False, is_flag=True)
@click.option("--major", default=False, required=False, is_flag=True)
def version(major, minor, patch, variable):
    current_version = get_package_version(variable=variable)
    init_module = find_init_module()
    if any([ x is True for x in [ major, minor, patch ]]):
        if major is True and all([ x is False for x in [ minor, patch ]]):
            next_version = semver.bump_major(current_version)
            save_file(init_module, variable, next_version)
            click.echo("Successfully updated major version from {} to {}".format(current_version, next_version))
        elif minor is True and all([ x is False for x in [ major, patch ]]):
            next_version = semver.bump_minor(current_version)
            save_file(init_module, variable, next_version)
            click.echo("Successfully updated minor version from {} to {}".format(current_version, next_version))
        elif patch is True and all([ x is False for x in [ major, minor ]]):
            next_version = semver.bump_patch(current_version)
            save_file(init_module, variable, next_version)
            click.echo("Successfully updated patch version from {} to {}".format(current_version, next_version))
        else:
            click.echo("Can only update one version major, minor, or patch")
    else:
        click.echo("Current version: {}".format(current_version))
