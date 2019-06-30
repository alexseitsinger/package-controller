import os
import click

from ...library.commands.document import document

EXCEPTIONS_EXPECTED = (
    RuntimeError,
    AssertionError,
    AttributeError,
    FileNotFoundError,
    NotADirectoryError,
)


@click.command(name="document")
def document_command():
    try:
        readme_file = document(status_message=lambda x: click.secho(x, fg="yellow"))
        click.secho("Successfully created documentation.", fg="green", bold=True)
    except EXCEPTIONS_EXPECTED as exc:
        click.secho("Failed to create documentation.", fg="red", bold=True)
        click.secho(str(exc), fg="red")
