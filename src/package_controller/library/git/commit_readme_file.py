from .add import add
from .commit import commit
from .assert_status import assert_status
from ..fascades.get_version import get_version


def commit_readme_file(relative_readme_path):
    try:
        assert_status()
    except AssertionError:
        current_version = get_version()
        add(relative_readme_path)
        commit_hash = commit(
            "docs", "Updates documentation for v{}.".format(current_version)
        )
    return relative_readme_path
