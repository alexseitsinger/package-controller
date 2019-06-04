import re
from io import open
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove


def replace_line(path, pattern, replacement, prepended_lines=[]):
    total_prepended = len(prepended_lines)
    fh, abs_path = mkstemp()
    with fdopen(fh, "w") as new_file:
        with open(path) as old_file:
            old_lines = old_file.readlines()
            for old_line in old_lines:
                match = re.match(pattern, old_line)
                if match:
                    start_index = old_lines.index(old_line)
                    count = -1
                    for prepended_line in prepended_lines:
                        count += 1
                        place = max(0, (start_index - (total_prepended - count)))
                        try:
                            if old_lines[place] != prepended_line:
                                new_file.write(prepended_line)
                        except IndexError:
                            new_file.write(prepended_line)
                    new_file.write(replacement)
                else:
                    new_file.write(old_line)
    remove(path)
    move(abs_path, path)
