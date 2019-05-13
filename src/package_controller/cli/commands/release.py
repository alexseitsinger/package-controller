import click

from ...utils import (
    twine_upload,
    git_push,
)


@click.command()
@click.option("--remote", default="origin", required=False, help="The remote to push to.")
@click.option("--branch", default="master", required=False, help="The branch to push.")
def release(remote, branch):
    try:
        twine_upload()
        click.secho("Successfully upload to PyPi", fg="green")
    except RuntimeError as exc:
        click.secho("Failed to upload to PyPi.", fg="red", bold=True)
        click.secho(str(exc), fg="red")
        return
    try:
        git_push(remote=remote, branch=branch)
        click.secho("Successfully pushed to git", fg="green")
    except RuntimeError as exc:
        click.secho("Failed to push to git. ({}, {})".format(remote, branch), fg="red", bold=True)
        click.secho(str(exc), fg="red")
        return
    try:
        git_push(tags=True)
        click.secho("Successfully pushed tags to git.", fg="green")
    except RuntimeError as exc:
        click.secho("Failed to push tags to git.", fg="red", bold=True)
        click.secho(str(exc), fg="red")
        return
