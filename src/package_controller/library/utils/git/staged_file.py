import os

from .staged_files import staged_files
from .assert_repository import assert_repository


def staged_file(f=None):
    assert_repository()
    staged = staged_files()
    if f is None and len(staged) == 1:
        return staged[0]
    fn = os.path.basename(f)
    for sf in staged:
        if f == sf:
            return sf
        if os.path.sep in f:
            if f.endswith(os.path.sep):
                # path/to/dir/ -> (path/to/dir/)first.py, (path/to/dir/)second.py
                if sf.startswith(f):
                    return sf
            # path/to/file.py -> some/(path/to/file.py)
            if sf.endswith(f):
                return sf
        # file.py -> path/to/(file.py)
        elif os.path.basename(sf) == fn:
            return sf
