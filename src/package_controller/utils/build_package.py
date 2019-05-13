import os

from .run import run

BUILD_ARGS = ["python", "setup.py", "sdist", "bdist_wheel"]
PIPENV_RUN_ARGS = ["pipenv", "run"]

def build_package():
    try:
        return run(*BUILD_ARGS)
    except Exception:
        args = PIPENV_RUN_ARGS + BUILD_ARGS
        return run(*args)


