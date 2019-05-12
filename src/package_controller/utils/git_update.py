from .git_add import git_add
from .git_commit import git_commit
from .git_tag import git_tag
from .make_changelog import make_changelog


def git_update(init_module, current_version, next_version):
    git_add(init_module)
    commit_hash = git_commit(
        type="docs",
        subject="Updates version",
        description="Version bump from {} to {}".format(
            current_version,
            next_version,
        )
    )
    tag_name = "v{}".format(next_version)
    git_tag(name=tag_name, hash=commit_hash)
    changelog = make_changelog()
    git_add(changelog)
    git_commit(
        type="docs",
        subject="Updates changelog",
        description="Updates the changelog for {}".format(tag_name),
    )

