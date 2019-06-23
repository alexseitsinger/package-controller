from io import open


def assert_readme_content(readme_file):
    with open(readme_file, "r") as f:
        if len(f.readlines()) <= 2:
            raise AssertionError("The README has no content.")
