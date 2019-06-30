import os
import click

from ...library.commands.build import build

EXCEPTIONS_EXPECTED = (
    RuntimeError,
    AssertionError,
    AttributeError,
    FileExistsError,
    FileNotFoundError,
    NotADirectoryError,
)


@click.command(name="build")
@click.option(
    "--replace",
    required=False,
    default=False,
    is_flag=True,
    help="If true, replaces existing built files.",
)
@click.option(
    "--force",
    required=False,
    default=False,
    is_flag=True,
    help="Force building the package despite having uncommmited changes.",
)
def build_command(replace, force):
    try:
        built = build(replace, force)
        click.secho("Successfully built package.", fg="green", bold=True)
        click.secho(
            "Files:\n    {}".format(
                "\n    ".join([os.path.basename(x) for x in built])
            ),
            fg="green",
        )
    except EXCEPTIONS_EXPECTED as exc:
        click.secho("Failed to build package.", fg="red", bold=True)
        click.secho(str(exc), fg="red")
