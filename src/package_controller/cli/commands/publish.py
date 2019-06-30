import click

from ...library.commands.publish import publish

EXCEPTIONS_EXPECTED = (
    NotADirectoryError,
    AssertionError,
    RuntimeError,
    AttributeError,
    FileNotFoundError,
)


@click.command(name="publish")
def publish_command():
    try:
        result = publish()
        click.secho("Successfully published package.", fg="green", bold=True)
    except EXCEPTIONS_EXPECTED as exc:
        message = str(exc)
        click.secho("Failed to publish package.", fg="red", bold=True)
        click.secho(message, fg="red")
