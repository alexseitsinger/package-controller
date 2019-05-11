import os
from .run import run


def git_add(*files):
    if not len(files):
        raise RuntimeError("No files passed")
    return run("git add {}".format(" ".join(files)))


def git_commit(type, scope, subject, description):
    if os.path.isfile(scope):
        scope = os.path.basename(scope)
    out = run("git commit -m '{header}' -m '{body}'".format(
        header="{type}({scope}): {subject}".format(
            type=type,
            scope=scope,
            subject=subject,
        ),
        body=description,
    ))
    print(out)
    commit_hash = run("git rev-parse HEAD")
    return commit_hash


def git_tag(name, hash=None):
    if not name.startswith("v"):
        name = "v{}".format(name)
    command = "git tag {name}".format(name=name)
    if hash is not None:
        command = "{} {}".format(command, hash)
    return run(command)


def make_changelog(output="CHANGELOG.md", type="angular", style="angular"):
    run("git-changelog . -o {output} -t {type} -s {style}".format(
        output=output, type=type, style=style,
    ))
    changelog = os.path.join(os.getcwd(), output)
    return changelog


def git_update(init_module, current_version, next_version):
    git_add(init_module)
    commit_hash = git_commit(
        type="chore",
        scope=init_module,
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
        scope=changelog,
        subject="Updates changelog",
        description="Updates the changelog for {}".format(tag_name),
    )

