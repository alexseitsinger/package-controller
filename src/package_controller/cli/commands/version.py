import click

from ...utils import version_bump

@click.command()
@click.option("--major", default=False, required=False, is_flag=True, help="Updates the major version.")
@click.option("--minor", default=False, required=False, is_flag=True, help="Updates the minor version.")
@click.option("--patch", default=False, required=False, is_flag=True, help="Updates the patch version.")
@click.option("--git", default=True, required=False, is_flag=True, help="Updates git with new tag and changelog for version.")
def version(major, minor, patch, git):
    version_bump(major, minor, patch, git)
