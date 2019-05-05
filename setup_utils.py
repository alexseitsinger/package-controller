import os
import sys
from importlib import import_module

ROOT = os.path.abspath(os.path.dirname(__file__))
PACKAGE_NAME = os.path.basename(ROOT)
sys.path.append(os.path.join(ROOT, "src", PACKAGE_NAME))

def import_util(name):
    module = import_module("{}.utils.{}".format(PACKAGE_NAME, name))
    method = getattr(module, name)
    return method

def package_setup(*args, **kwargs):
    package_setup = import_util("package_setup")
    return package_setup(*args, **kwargs)



