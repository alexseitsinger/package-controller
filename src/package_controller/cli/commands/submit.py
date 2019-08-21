import click

from ...library.utils.run import run

EXCEPTIONS_EXPECTED = (
    RuntimeError,
    NotADirectoryError,
    FileNotFoundError,
    FileExistsError,
    AttributeError,
    AssertionError,
    TypeError,
)


@click.command(name="submit")
@click.option("--version", required=True, default="minor", help="The version to update")
@click.option("--otp", help="The one-time-password for NPM.")
def submit_command(version, otp):
    commands = [
        "pc test --unit --integration",
        # "pc bump --{}".format(version),
        # "pc pin --development",
        # "pc unpin --peer --optional",
        # "pc build",
        # "pc document",
        # "pc release",
        # "pc publish --otp {}".format(otp),
    ]
    done = False
    ran = 0

    while done is False:
        if ran == len(commands):
            done = True
        for command in commands:
            ran += 1
            try:
                out = run(command)
                click.secho(out, fg="green")
            except Exception as exc:
                click.secho(str(exc), fg="red")
