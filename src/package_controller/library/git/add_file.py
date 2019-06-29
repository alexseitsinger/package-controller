import os

from ..generic.run import run
from .staged_file import staged_file
from .assert_repository import assert_repository


def add_file(f=None):
    assert_repository()
    if f is None:
        return add_file(staged_file())
    try:
        run("git add {}".format(f))
        return f
    except RuntimeError as exc:
        msg = str(exc)
        # If we get a failed add due to unmatching file. attempt to find it.
        if msg.startswith("fatal: pathspec") and msg.endswith(
            "did not match any files"
        ):
            sf = staged_file(f)
            if sf:
                return add_file(sf)
        # Otehrwise, just raise the original exception.
        raise RuntimeError("Failed to add file {}".format(f))
