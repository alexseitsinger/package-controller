import click

from ...library.commands.unpin import unpin


EXCEPTIONS_EXPECTED = (
    RuntimeError,
    AssertionError,
    AttributeError,
    FileNotFoundError,
    NotADirectoryError,
)


@click.command(name="unpin")
@click.option(
    "--production",
    is_flag=True,
    default=False,
    help="Unpin the versions of production dependencies.",
)
@click.option(
    "--development",
    is_flag=True,
    default=False,
    help="Unpin the versions of development dependencies.",
)
@click.option(
    "--peer",
    is_flag=True,
    default=False,
    help="Unpin the versions of peer dependencies.",
)
@click.option(
    "--optional",
    is_flag=True,
    default=False,
    help="Unpin the versions of optional dependencies.",
)
def unpin_command(production, development, peer, optional):
    try:
        unpinned = unpin(production, development, optional, peer)
        names = []
        for k, v in unpinned.items():
            if v is True:
                names += [k.capitalize()]
        if len(names):
            message = "Successfully unpinned the versions for:\n    {}".format(
                "\n".join(names)
            )
            click.secho(message, fg="green", bold=True)
    except EXCEPTIONS_EXPECTED as exc:
        click.secho("Failed to unpin versions.", fg="red", bold=True)
        click.secho(str(exc), fg="red")
