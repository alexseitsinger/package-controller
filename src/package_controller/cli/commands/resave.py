import click

from ...library.commands.resave import resave


EXCEPTIONS_EXPECTED = (
    RuntimeError,
    AttributeError,
    AssertionError,
    FileNotFoundError,
    NotADirectoryError,
)


@click.command(name="resave")
@click.argument("count", required=True)
def resave_command(count):
    try:
        result = resave(count)
        click.secho("Successfully resaved {} commits.".format(count))
    except EXCEPTIONS_EXPECTED as exc:
        click.secho("Failed to resave.", fg="red", bold=True)
        click.secho(str(exc), fg="red")
