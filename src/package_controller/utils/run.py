import subprocess


def run(command):
    process = subprocess.run(command.split(), capture_output=True)
    if process.returncode != 0:
        message = process.stderr.strip().decode("utf-8")
        raise RuntimeError(message)
    return process.stdout.strip().decode("utf-8")
