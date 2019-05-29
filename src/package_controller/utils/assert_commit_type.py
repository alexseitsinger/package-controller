COMMIT_TYPES_ALLOWED = [
    "chore", "feat", "fix", "docs", "style", "refactor", "perf", "localize",
    "test",
]


def assert_commit_type(name):
    if not name in COMMIT_TYPES_ALLOWED:
        raise AssertionError("The commit type must be one of {}.".format(
                             ", ".join(COMMIT_TYPES_ALLOWED)))

