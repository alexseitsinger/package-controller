import click

from .commands import version, build, release

@click.group()
def main():
    pass


main.add_command(version)
main.add_command(build)
main.add_command(release)


