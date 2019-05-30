import os

from .git_staged_files import git_staged_files
from .assert_git_repository import assert_git_repository


def git_staged_file(f):
    assert_git_repository()
    fn = os.path.basename(f)
    for sf in git_staged_files():
        if f == sf:
            return sf
        elif os.path.sep in f:
            # path/to/dir/ -> path/to/dir/first.py, path/to/dir/second.py
            if f.endswith(os.path.sep):
                if sf.startswith(f):
                    return sf
            # path/to/file.py -> path/to/file.py
            elif sf.endswith(f):
                return sf
        # file.py -> path/to/file.py 
        elif os.path.basename(sf) == fn:
            return sf
