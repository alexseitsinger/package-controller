from .save_file import save_file
from .find_init_module import find_init_module


def save_version(next_version):
    init_module = find_init_module()
    save_file(init_module, "__version__", next_version)
