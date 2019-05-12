import subprocess


def run(*args):
    process = subprocess.run(args, capture_output=True)
    if process.returncode != 0:
        message = process.stderr.strip().decode("utf-8")
        raise RuntimeError(message)
    return process.stdout.strip().decode("utf-8")
