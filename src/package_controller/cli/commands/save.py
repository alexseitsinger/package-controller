import os
import click

from ...library.utils.git.add import add
from ...library.utils.git.commit import commit

FAILURE_EXCEPTIONS = (
    RuntimeError,
    AssertionError,
    AttributeError,
    FileNotFoundError,
    NotADirectoryError,
)


@click.command(name="save")
@click.option("--type", "-t", "type_", required=True, help="The commit type.")
@click.option("--message", "-m", required=True, help="The commit message.")
@click.argument("files", required=False, nargs=-1)
def save_command(type_, message, files):
    try:
        staged = add(*files)
        commit_hash = commit(type_, message)
        click.secho("Successfully saved files.", fg="green", bold=True)
        click.secho("Commit: {}".format(commit_hash), fg="green")
        click.secho("Files:\n    {}".format("\n    ".join(list(staged))), fg="green")
    except FAILURE_EXCEPTIONS as exc:
        click.secho("Failed to save files.", fg="red", bold=True)
        click.secho(str(exc), fg="red")
