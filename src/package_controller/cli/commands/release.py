import os
import click

from ...library.fascades.release_package import release_package
from ...library.fascades.get_version import get_version

FAILURE_EXCEPTIONS = (
    NotADirectoryError,
    AssertionError,
    RuntimeError,
    AttributeError,
    FileNotFoundError,
)


@click.command()
@click.option("--remote", "-r", default="origin", required=False, help="The remote to push to.")
@click.option("--branch", "-b", default="master", required=False, help="The branch to push to.")
@click.option("--no-tag", "-nt", default=False, required=False, is_flag=True, help="If true, will not push the tag.")
def release(remote, branch, no_tag):
    try:
        tag_name = None
        if no_tag is False:
            tag_name = "v{}".format(get_version())
        uploaded = release_package(remote=remote, branch=branch, tag_name=tag_name)
        click.secho("Successfully released package.", fg="green", bold=True)
        if uploaded is not None:
            click.secho(
                "Files:\n    {}".format("\n    ".join([
                    os.path.basename(x) for x in uploaded
                ])),
                fg="green"
            )
    except FAILURE_EXCEPTIONS as exc:
        message = str(exc)
        click.secho("Failed to release package.", fg="red", bold=True)
        click.secho(message, fg="red")
