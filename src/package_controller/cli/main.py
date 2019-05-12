import click

from .version import version


@click.group()
def main():
    pass


main.add_command(version)


