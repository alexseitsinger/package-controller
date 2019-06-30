import click
import semver

from ...library.utils.git.update import update
from ...library.commands.bump import bump
from ...library.commands.version import version

EXCEPTIONS_EXPECTED = (
    RuntimeError,
    AssertionError,
    AttributeError,
    FileNotFoundError,
    NotADirectoryError,
)

CHANGELOG_EXCEPTION_MESSAGES = (
    "No git remotes detected, so can't make a changelog.",
    "git-changelog is not installed.",
)


@click.command(name="bump")
@click.option(
    "--major",
    default=False,
    required=False,
    is_flag=True,
    help="Updates the major version.",
)
@click.option(
    "--minor",
    default=False,
    required=False,
    is_flag=True,
    help="Updates the minor version.",
)
@click.option(
    "--patch",
    default=False,
    required=False,
    is_flag=True,
    help="Updates the patch version.",
)
@click.option(
    "--force",
    default=False,
    required=False,
    is_flag=True,
    help="Force the version update even if there are uncommitted changes.",
)
@click.option(
    "--no-git",
    default=False,
    required=False,
    is_flag=True,
    help="Do not update git with a new tag and changelog for version.",
)
def bump_command(major, minor, patch, force, no_git):
    try:
        old_version, new_version = bump(major, minor, patch, force)
        if no_git is False:
            tag_name = update(old_version, new_version)
        click.secho(
            "Successfully updated version from {} to {}".format(
                old_version, new_version
            ),
            fg="green",
            bold=True,
        )
    except EXCEPTIONS_EXPECTED as exc:
        message = str(exc)
        if message in CHANGELOG_EXCEPTION_MESSAGES:
            click.secho("Skipped creating changelog.", fg="yellow", bold=True)
            click.secho(message, fg="yellow")
        else:
            click.secho("Failed to update version.", fg="red", bold=True)
            click.secho(message, fg="red")
