def format_commit_text(text):
    text = text.strip()
    text = text[0].upper() + text[1:]
    if not text.endswith("."):
        text = "{}.".format(text)
    return text

