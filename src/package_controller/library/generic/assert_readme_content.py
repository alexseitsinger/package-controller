from io import open


def assert_readme_content(readme_file):
    total = 0
    with open(readme_file, "r") as f:
        for line in f:
            total += 1
    if total <= 3:
        raise AssertionError("The README has no content.")
