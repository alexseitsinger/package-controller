import click

from ...utils import build_package


@click.command()
def build():
    try:
        build_package()
        click.secho("Successfully built package.", fg="green")
    except RuntimeError as exc:
        click.secho("Failed to build package.", fg="red", bold=True)
        click.secho(str(exc), fg="red")
