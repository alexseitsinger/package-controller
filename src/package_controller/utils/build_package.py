import os
import click

from .run import run

BUILD_ARGS = ["python", "setup.py", "sdist", "bdist_wheel"]
PIPENV_RUN_ARGS = ["pipenv", "run"]

def build_package():
    try:
        out = run(*BUILD_ARGS)
        click.secho("Successfully built package.", fg="green")
        return out
    except RuntimeError:
        try:
            args = PIPENV_RUN_ARGS + BUILD_ARGS
            out = run(*args)
            click.secho("Successfully built package.", fg="green")
            return out
        except Exception:
            return click.secho("Failed to build package.", fg="red")




