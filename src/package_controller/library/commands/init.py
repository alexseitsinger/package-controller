import os
import shutil

from ..utils.get_config_settings import get_config_settings
from ..utils.git.gitignore import set_gitignore_for_language
from ..utils.run import run


LANGUAGES_ALLOWED = ["python", "node"]


def init_package(package_name, template_version, settings):
    templates_dir = settings["templates"]
    library_dir = settings["library"]["active"]
    package_dir = os.path.join(library_dir, package_name)
    # cd to templates dir,
    os.chdir(templates_dir)
    # checkout the branch
    branch_name = template_version
    if not branch_name.startswith("v"):
        branch_name = "v{}".format(branch_name)
    run("git checkout {}".format(branch_name))
    # copy the template to the package directory.
    shutil.cptree(templates_dir, package_dir)
    if not os.path.exists(package_dir):
        raise RuntimeError("Failed to initialize package. ({})".format(package_dir))
    return package_dir


def init_node(package_name, template_version):
    settings = get_config_settings("node")
    package_dir = init_package(package_name, template_version, settings)
    try:
        os.chdir(package_dir)
        set_gitignore_for_language("node", replace=True)
    except FileExistsError:
        pass


def init_python(package_name, template_version):
    settings = get_config_settings("python")
    package_dir = init_package(package_name, template_version, settings)
    try:
        os.chdir(package_dir)
        set_gitignore_for_language("python", replace=True)
    except FileExistsError:
        pass


def init(package_name, template_version, language_name):
    if language_name == "node":
        return init_node(package_name, template_version)
    elif language_name == "python":
        return init_python(package_name, template_version)
    else:
        raise RuntimeError(
            "Language must be one of:\n    {}".format("\n".join(LANGUAGES_ALLOWED))
        )
