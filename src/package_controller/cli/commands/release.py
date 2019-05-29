import os
import click

from ...utils.release_package import release_package
from ...utils.git_push import git_push

FAILURE_EXCEPTIONS = (
    NotADirectoryError,
    AssertionError,
    RuntimeError,
    AttributeError,
    FileNotFoundError,
)


@click.command()
@click.option("--remote", default="origin", required=False, help="The remote to push to.")
@click.option("--branch", default="master", required=False, help="The branch to push.")
def release(remote, branch):
    try:
        uploaded = release_package()
        click.secho("Successfully uploaded to PyPi.", fg="green", bold=True)
        click.secho(
            "Files:\n    {}".format("\n    ".join([
                os.path.basename(x) for x in uploaded
            ])),
            fg="green"
        )
    except FAILURE_EXCEPTIONS as exc:
        message = str(exc)
        if message == "twine is not installed.":
            click.secho("Skipped uploading to PyPi.", fg="yellow", bold=True)
            click.secho(message, fg="yellow")
        else:
            click.secho("Failed to upload to PyPi.", fg="red", bold=True)
            click.secho(message, fg="red")
            return
    try:
        git_push(remote=remote, branch=branch)
        click.secho("Successfully pushed to git. ({}, {})".format(remote, branch), fg="green", bold=True)
    except FAILURE_EXCEPTIONS as exc:
        click.secho("Failed to push to git. ({}, {})".format(remote, branch), fg="red", bold=True)
        click.secho(str(exc), fg="red")
        return
    try:
        git_push(tags=True)
        click.secho("Successfully pushed tags to git.", fg="green", bold=True)
    except FAILURE_EXCEPTIONS as exc:
        click.secho("Failed to push tags to git.", fg="red", bold=True)
        click.secho(str(exc), fg="red")
        return
