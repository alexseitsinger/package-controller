import click

from ...library.commands.unsave import unsave


EXCEPTIONS_EXPECTED = (
    RuntimeError,
    AttributeError,
    AssertionError,
    NotADirectoryError,
    FileNotFoundError,
)


@click.command(name="unsave")
@click.argument("count", required=True)
def unsave_command(count):
    try:
        result = unsave(count)
        click.secho(
            "Successfully unsaved {} commits.".format(count), fg="green", bold=True
        )
    except EXCEPTIONS_EXPECTED as exc:
        click.secho("Failed to unsave.", fg="red", bold=True)
        click.secho(str(exc), fg="red")
