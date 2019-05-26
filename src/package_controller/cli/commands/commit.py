import os
import click

from ...utils.git_commit import git_commit


@click.command()
@click.option("--type", "-t", "type_", required=True)
@click.option("--subject", "-s", required=True)
@click.option("--description", "-d", required=False)
def commit(type_, subject, description):
    try:
        git_commit(type_, subject, description=description)
        click.secho("Successfully commited changes.", fg="green", bold=True)
    except RuntimeError as exc:
        click.secho("Failed to commit changes.", fg="red", bold=True)
        click.secho(str(exc), fg="red")
