import click


from ...library.commands.init import init


EXCEPTIONS_EXPECTED = (RuntimeError,)


@click.command(name="init")
@click.argument("package_name", required=True, help="The package name.")
@click.argument("template_version", required=True, help="The template version to use.")
@click.argument("language_name", required=True, help="The language name.")
def init_command(package_name, template_version, language_name):
    try:
        package_dir = init(package_name, template_version, language_name)
        click.secho("Initialized package successfully.", fg="green", bold=True)
        click.secho(package_dir, fg="green")
    except EXCEPTIONS_EXPECTED as exc:
        click.secho("Failed to initialize package.", fg="red", bold=True)
        click.secho(str(exc), fg="red")
