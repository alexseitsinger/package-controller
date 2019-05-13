import click

from ...utils import build_package


@click.command()
def build():
    build_package()
