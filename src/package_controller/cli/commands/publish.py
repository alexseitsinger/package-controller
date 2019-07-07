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
@click.option(
    "--access", "-a", default="public", required=False, help="The access level for NPM."
)
@click.option("--otp", "-o", required=False, help="The OTP code for NPM.")
def publish_command(access, otp):
    try:
        result = publish(access, otp)
        click.secho("Successfully published package.", fg="green", bold=True)
    except EXCEPTIONS_EXPECTED as exc:
        message = str(exc)
        click.secho("Failed to publish package.", fg="red", bold=True)
        click.secho(message, fg="red")
