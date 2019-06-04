import os
import click

from ...library.fascades.build_package import build_package

FAILURE_EXCEPTIONS = (
    RuntimeError,
    AssertionError,
    AttributeError,
    FileNotFoundError,
    NotADirectoryError,
)

@click.command()
@click.option(
    "--force", required=False, default=False, is_flag=True,
    help="Force building the package despite having uncommmited changes.")
def build(force):
    try:
        built = build_package(force=force)
        click.secho("Successfully built package.", fg="green", bold=True)
        click.secho(
            "Files:\n    {}".format("\n    ".join([
                os.path.basename(x) for x in built
            ])),
            fg="green",
        )
    except FAILURE_EXCEPTIONS as exc:
        click.secho("Failed to build package.", fg="red", bold=True)
        click.secho(str(exc), fg="red")
