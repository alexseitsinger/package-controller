import click

from .commands.commit import commit
from .commands.build import build
from .commands.release import release
from .commands.version import version
from .commands.add import add


@click.group()
def main():
    pass


main.add_command(add)
main.add_command(commit)
main.add_command(version)
main.add_command(build)
main.add_command(release)


