import os
import click

from ...library.git.diff import diff as git_diff

FAILURE_EXCEPTIONS = (
    RuntimeError,
    AssertionError,
    AttributeError,
    FileNotFoundError,
    NotADirectoryError,
)


@click.command()
@click.argument("file_", required=True)
def diff(file_):
    try:
        lines = git_diff(file_).split("\n")
        for line in lines:
            if line.startswith("+"):
                click.secho(line, fg="green")
            elif line.startswith("-"):
                click.secho(line, fg="red")
            elif line.startswith("@@"):
                click.secho(line, fg="yellow")
            else:
                click.echo(line)
    except FAILURE_EXCEPTIONS as exc:
        click.secho("Failed to diff file.", fg="red", bold=True)
        click.secho(str(exc), fg="red")
