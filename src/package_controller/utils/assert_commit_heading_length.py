HEADING_LENGTH_MAX = 50


def assert_commit_heading_length(heading):
    difference = len(heading) - HEADING_LENGTH_MAX
    if difference > 0:
        raise AssertionError(
            "The heading is {} characters too long. "
            "It must be {} characters or less.".format(
                difference, HEADING_LENGTH_MAX
            )
        )

