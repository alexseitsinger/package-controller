import textwrap
import re

from .run import run


GIT_COMMIT_ARGS = ["git", "commit"]
GIT_LAST_COMMIT_HASH_ARGS = ["git", "rev-parse", "HEAD"]
RE_DESCRIPTION_DELIMITER = r"(?![\w\d])\.\s+"
COMMIT_TYPES_ALLOWED = [
    "chore", "feat", "fix", "docs", "style", "refactor", "perf", "localize",
    "test",
]


def assert_commit_type(name):
    if not name in COMMIT_TYPES_ALLOWED:
        raise RuntimeError("The commit type must be one of {}".format(
            ", ".join(COMMIT_TYPES_ALLOWED)))


def format_commit_text(text):
    text = text.strip()
    text = text.capitalize()
    if not text.endswith("."):
        text = "{}.".format(text)
    return text


def format_commit_description(description, delimiter="."):
    # Try to split the description up into bits using the delimiter.
    bits = None
    if bits is None or isinstance(bits, list) and not len(bits):
        bits = [
            format_commit_text(x)
            for x in re.split(RE_DESCRIPTION_DELIMITER, description)
            if len(x)
        ]
    # convert the bits into a single string again, that is wrapped at 72 
    # characters.
    text = " ".join(bits)
    wrapped = textwrap.wrap(text, width=72)
    joined = "\n".join(wrapped)
    return joined


def git_commit(commit_type, subject, description=None):
    assert_commit_type(commit_type)
    # Remove any excess whitespace from the subject.
    subject = format_commit_text(subject)
    # Create the heading for the commit.
    heading = "{}: {}".format(commit_type, subject)
    heading_len = len(heading)
    heading_len_max = 50
    heading_len_diff = heading_len - heading_len_max
    if heading_len_diff > 0:
        raise RuntimeError("The heading is {} characters too long. "
                           "It must be {} characters or less.".format(
                           heading_len_diff, heading_len_max))
    # Create the commit args.
    commit_args = GIT_COMMIT_ARGS + ["-m", heading]
    # Iterate over the description, if possible, and convert each line into
    # a new -m entry to use a newline in the commit message.
    if description is not None:
        commit_args += format_commit_description(description)
    # Run the command we've put togehter to create the commit.
    run(*commit_args)
    # Then, get and return the hash for the commit we just created.
    return run(*GIT_LAST_COMMIT_HASH_ARGS)

