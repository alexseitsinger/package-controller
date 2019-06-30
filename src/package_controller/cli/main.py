import click

from .commands.version import version_command
from .commands.bump import bump_command
from .commands.diff import diff_command
from .commands.save import save_command

# from .commands.unsave import unsave_command
# from .commands.undo import undo_command
# from .commands.resave import resave_command
from .commands.test import test_command
from .commands.build import build_command
from .commands.document import document_command
from .commands.pin import pin_command
from .commands.unpin import unpin_command
from .commands.release import release_command
from .commands.publish import publish_command


@click.group()
def main():
    pass


main.add_command(version_command)
main.add_command(bump_command)
main.add_command(diff_command)
main.add_command(save_command)
# main.add_command(unsave_command)
# main.add_command(undo_command)
# main.add_command(resave_command)
main.add_command(test_command)
main.add_command(build_command)
main.add_command(document_command)
main.add_command(pin_command)
main.add_command(unpin_command)
main.add_command(release_command)
main.add_command(publish_command)
