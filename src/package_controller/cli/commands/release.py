import click

from ...utils import release_package


@click.command()
def release():
    click.echo(release_package())
