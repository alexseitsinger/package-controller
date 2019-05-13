import click

from ...utils import release_package


@click.command()
def release():
    release_package()
