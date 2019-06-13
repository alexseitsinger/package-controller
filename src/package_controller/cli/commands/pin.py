import click

from ...library.fascades.pin_versions import pin_versions


FAILURE_EXCEPTIONS = (
    RuntimeError,
    AssertionError,
    AttributeError,
    FileNotFoundError,
    NotADirectoryError,
)


@click.command()
@click.option(
    "--production",
    is_flag=True,
    default=False,
    help="Pin the versions of production dependencies.",
)
@click.option(
    "--development",
    is_flag=True,
    default=False,
    help="Pin the versions of development dependencies.",
)
@click.option(
    "--peer", is_flag=True, default=False, help="Pin the versions of peer dependencies."
)
@click.option(
    "--optional",
    is_flag=True,
    default=False,
    help="Pin the versions of optional dependencies.",
)
def pin(production, development, peer, optional):
    try:
        pinned = pin_versions(
            production=production, development=development, optional=optional, peer=peer
        )
        names = []
        for k, v in pinned.items():
            if v is True:
                names += [k.capitalize()]
        if len(names):
            message = "Successfully pinned the versions for:\n    {}".format(
                "\n".join(names)
            )
            click.secho(message, fg="green", bold=True)
    except FAILURE_EXCEPTIONS as exc:
        click.secho("Failed to pin versions.", fg="red", bold=True)
        click.secho(str(exc), fg="red")
