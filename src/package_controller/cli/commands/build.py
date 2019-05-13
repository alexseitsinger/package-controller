import os
import click

from ...utils import build_package


@click.command()
def build():
    try:
        built = build_package()
        click.secho("Successfully built package.", fg="green", bold=True)
        click.secho(
            "Files:\n    {}".format("\n    ".join([
                os.path.basename(x) for x in built
            ])),
            fg="green",
        )
    except RuntimeError as exc:
        click.secho("Failed to build package.", fg="red", bold=True)
        click.secho(str(exc), fg="red")
