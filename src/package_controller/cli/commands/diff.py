import os
import click

from ...library.utils.git.diff import diff

EXCEPTIONS_EXPECTED = (
    RuntimeError,
    AssertionError,
    AttributeError,
    FileNotFoundError,
    NotADirectoryError,
)


@click.command(name="diff")
@click.argument("file_")
def diff_command(file_):
    try:
        lines = diff(file_).split("\n")
        for line in lines:
            if line.startswith("+"):
                click.secho(line, fg="green")
            elif line.startswith("-"):
                click.secho(line, fg="red")
            elif line.startswith("@@"):
                click.secho(line, fg="yellow")
            else:
                click.echo(line)
    except EXCEPTIONS_EXPECTED as exc:
        click.secho("Failed to diff file.", fg="red", bold=True)
        click.secho(str(exc), fg="red")
