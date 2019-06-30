import click

from ...library.fascades.version import version


@click.command(name="version")
def version_command():
    message = "Current version: {}".format(version())
    click.secho(message, fg="yellow", bold=True)
