import os
import click

from ...utils.git_add import git_add


@click.command()
@click.argument("name", required=True)
def add(name):
    try:
        git_add(name)
        click.secho("Successfully added files.", fg="green", bold=True)
    except RuntimeError as exc:
        click.secho("Failed to add files.", fg="red", bold=True)
        click.secho(str(exc), fg="red")
