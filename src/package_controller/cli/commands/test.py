import os
import click

from ...utils.test_package import test_package

FAILURE_EXCEPTIONS = (
    NotADirectoryError,
    AssertionError,
    RuntimeError,
    AttributeError,
    FileNotFoundError,
)


@click.command()
@click.option("--unit", "-u", required=False, default=False, is_flag=True)
@click.option("--integration", "-i", required=False, default=False, is_flag=True)
def test(unit, integration):
    try:
        unit_tests_output, integration_tests_output = test_package(unit=unit, integration=integration)
        if unit_tests_output is not None:
            click.secho("Unit:\n", fg="green", bold=True)
            click.secho(unit_tests_output, fg="yellow")
        if integration_tests_output is not None:
            click.secho("\nIntegration:\n", fg="green", bold=True)
            click.secho(integration_tests_output, fg="yellow")
    except FAILURE_EXCEPTIONS as exc:
        click.secho("Failed to test package.", fg="red", bold=True)
        click.secho(str(exc), fg="red")


