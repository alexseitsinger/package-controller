import os
import click

from ...library.fascades.update_documentation import update_documentation

FAILURE_EXCEPTIONS = (
    RuntimeError,
    AssertionError,
    AttributeError,
    FileNotFoundError,
    NotADirectoryError,
)


@click.command()
def document():
    try:
        readme_file = update_documentation(
            status_message=lambda x: click.secho(x, fg="yellow")
        )
        click.secho("Successfully created documentation.", fg="green", bold=True)
    except FAILURE_EXCEPTIONS as exc:
        click.secho("Failed to create documentation.", fg="red", bold=True)
        click.secho(str(exc), fg="red")
