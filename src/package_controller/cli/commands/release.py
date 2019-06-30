import click

from ...library.fascades.release import release

EXCEPTIONS_EXPECTED = (
    NotADirectoryError,
    AssertionError,
    RuntimeError,
    AttributeError,
    FileNotFoundError,
)


@click.command(name="release")
@click.option(
    "--remote", "-r", default="origin", required=False, help="The remote to push to."
)
@click.option(
    "--branch", "-b", default="master", required=False, help="The branch to push to."
)
@click.option(
    "--force", "-f", required=False, is_flag=True, default=False, help="Force git push."
)
def release_command(remote, branch, force):
    try:
        result = release(remote, branch, force)
        click.secho("Successfully released package.", fg="green", bold=True)
    except EXCEPTIONS_EXPECTED as exc:
        message = str(exc)
        click.secho("Failed to release package.", fg="red", bold=True)
        click.secho(message, fg="red")
