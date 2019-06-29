import os
import click

from ...library.git.commit import commit as git_commit

FAILURE_EXCEPTIONS = (
    RuntimeError,
    AssertionError,
    AttributeError,
    FileNotFoundError,
    NotADirectoryError,
)


@click.command()
@click.option("--type", "-t", "type_", required=True)
@click.option("--message", "-m", required=True)
def commit(type_, message):
    try:
        git_commit(type_, message)
        click.secho("Successfully commited changes.", fg="green", bold=True)
    except FAILURE_EXCEPTIONS as exc:
        click.secho("Failed to commit changes.", fg="red", bold=True)
        click.secho(str(exc), fg="red")
