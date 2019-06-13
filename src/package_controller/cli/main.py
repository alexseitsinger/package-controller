import click

from .commands.add import add
from .commands.build import build
from .commands.commit import commit
from .commands.diff import diff
from .commands.pin import pin
from .commands.unpin import unpin
from .commands.release import release
from .commands.test import test
from .commands.version import version


@click.group()
def main():
    pass


main.add_command(add)
main.add_command(build)
main.add_command(commit)
main.add_command(diff)
main.add_command(pin)
main.add_command(unpin)
main.add_command(release)
main.add_command(test)
main.add_command(version)
