import click

from .version import version


@click.group()
def main():
    pass


main.add_command(version)


if __name__ == "__main__":
    main()
