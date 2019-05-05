import re


def save_file(path, variable, value):
    encoding = "utf-8"
    regex = r"(^{} = ['\"])([^'\"]*)(['\"])".format(variable)
    with open(path, "r", encoding=encoding) as fr:
        content = fr.read()
    with open(path, "w", encoding=encoding) as fw:
        match = re.match(regex, content)
        try:
            groups = match.groups()
            content = "{}{}{}".format(groups[0], value, groups[2])
        except IndexError:
            pass
        fw.write(content)
