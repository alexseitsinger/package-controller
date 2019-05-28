def format_commit_text(text):
    text = text.strip()
    text = text.capitalize()
    if not text.endswith("."):
        text = "{}.".format(text)
    return text

