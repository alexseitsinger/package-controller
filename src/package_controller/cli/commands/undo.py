import click

from ...library.commands.undo import undo


EXCEPTIONS_EXPECTED = (
    RuntimeError,
    AttributeError,
    AssertionError,
    NotADirectoryError,
    FileNotFoundError,
)


@click.command(name="undo")
@click.argument("count", required=True)
def undo_command(count):
    try:
        result = undo(count)
        click.secho(
            "Successfully undid {} commits.".format(count), fg="green", bold=True
        )
    except EXCEPTIONS_EXPECTED as exc:
        click.secho("Failed to undo.", fg="red", bold=True)
        click.secho(str(exc), fg="red")
