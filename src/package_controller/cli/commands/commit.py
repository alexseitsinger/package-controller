import os
import click

from ...utils.git_commit import git_commit


@click.command()
@click.option("--type", required=True)
@click.option("--subject", required=True)
@click.option("--description", required=False)
def commit(type, subject, description):
    try:
        git_commit(type=type, subject=subject, description=description)
        click.secho("Successfully commited changes.", fg="green", bold=True)
    except RuntimeError as exc:
        click.secho("Failed to commit changes.", fg="red", bold=True)
        click.secho(str(exc), fg="red")
