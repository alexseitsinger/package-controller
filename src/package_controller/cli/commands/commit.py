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
@click.option("--subject", "-s", required=True)
@click.option("--description", "-d", required=False)
def commit(type_, subject, description):
    try:
        git_commit(type_, subject, description=description)
        click.secho("Successfully commited changes.", fg="green", bold=True)
    except FAILURE_EXCEPTIONS as exc:
        click.secho("Failed to commit changes.", fg="red", bold=True)
        click.secho(str(exc), fg="red")
