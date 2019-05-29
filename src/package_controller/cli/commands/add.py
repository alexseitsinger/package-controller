import os
import click

from ...utils.git_add import git_add

FAILURE_EXCEPTIONS = (
    RuntimeError,
    AssertionError,
    AttributeError,
    FileNotFoundError,
    NotADirectoryError,
)


@click.command()
@click.option("--files", "-f", required=True, multiple=True)
def add(files):
    try:
        succeeded = git_add(*files)
        click.secho("Successfully added files.", fg="green", bold=True)
        click.secho("Files:\n    {}".format("\n    ".join(list(succeeded))), fg="green")
    except FAILURE_EXCEPTIONS as exc:
        click.secho("Failed to add files.", fg="red", bold=True)
        click.secho(str(exc), fg="red")
