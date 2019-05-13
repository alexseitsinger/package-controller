import click

from ...utils import build_package


@click.command()
def build():
    click.echo(build_package())
