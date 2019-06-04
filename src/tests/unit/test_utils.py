import pytest
import tempfile

from package_controller.library.git.add import add
from package_controller.library.git.assert_commit import assert_commit
from package_controller.library.git.assert_commit_heading_length import assert_commit_heading_length
from package_controller.library.git.assert_commit_type import assert_commit_type
from package_controller.library.git.assert_remotes import assert_remotes
from package_controller.library.git.assert_repository import assert_repository
from package_controller.library.git.assert_status import assert_status
from package_controller.library.git.format_commit_description import format_commit_description
from package_controller.library.git.format_commit_text import format_commit_text
from package_controller.library.git.add_file import add_file
from package_controller.library.git.commit import commit
from package_controller.library.git.diff import diff
from package_controller.library.git.is_repository import is_repository
from package_controller.library.git.make_changelog import make_changelog
from package_controller.library.git.push import push
from package_controller.library.git.staged_file import staged_file
from package_controller.library.git.staged_files import staged_files
from package_controller.library.git.tag import tag
from package_controller.library.git.update import update

from package_controller.library.python.find_init_module import find_init_module
from package_controller.library.python.get_python_package_dir import get_python_package_dir
from package_controller.library.python.is_python_package import is_python_package
from package_controller.library.python.save_version import save_version
from package_controller.library.python.twine_upload import twine_upload

from package_controller.library.node.is_node_package import is_node_package

from package_controller.library.generic.assert_which import assert_which
from package_controller.library.generic.find_file import find_file
from package_controller.library.generic.is_executable import is_executable
from package_controller.library.generic.read_file import read_file
from package_controller.library.generic.replace_line import replace_line
from package_controller.library.generic.run import run
from package_controller.library.generic.which import which

from package_controller.library.fascades.build_package import build_package
from package_controller.library.fascades.bump_version import bump_version
from package_controller.library.fascades.get_version import get_version
from package_controller.library.fascades.release_package import release_package
# Importing this causes pytest to raise an Exception since that's what invokes this.
#from package_controller.library.fascades.test_package import test_package


def test_assert_commit():
    # Test the valid initial commit
    assert assert_commit("0609384cdfe7aaa9eb45c32fce00b9d9b58694bb") is None

    # Test an invalid commit hash.
    with pytest.raises(AssertionError):
        assert_commit("an_invalid_commit_hash")


def test_assert_commit_type():
    # Test with a valid type.
    assert assert_commit_type("chore") == None

    # Test with an invalid type.
    with pytest.raises(AssertionError, match=r"^The commit type must be one of "):
        assert_commit_type("non_existent_commit_type")


def test_assert_status():
    pass


def test_assert_which():
    # Test with a valid executable.
    assert assert_which("sh") is None
    
    # Test with an invalid executable
    with pytest.raises(AssertionError, match=r"^Executable was not found. \(.+\)"):
        assert_which("nonexistant_exec_name")


def test_build_package():
    pass


def test_bump_version():
    pass


def test_find_file():
    pass


def test_find_init_module():
    pass


def test_format_commit_description():
    pass


def test_format_commit_text():
    pass


def test_get_version():
    # Create a temp file to use for the python reading. 
    tmp = tempfile.NamedTemporaryFile()

    # Set the content of the file.
    with open(tmp.name, "w") as f:
        f.write("__version__ = \"0.1.0\"")
    
    with open(tmp.name) as f:
        # Test reading a valid variable from the file.
        assert get_version(f.name, "__version__") == "0.1.0"
        
        # Test reading an invalid variable.
        with pytest.raises(AttributeError):
            get_version(f.name, "_version_")
     
    # Close the file so it gets deleted.
    tmp.close()


def test_git_add():
    pass


def test_git_add_file():
    pass


def test_git_commit():
    pass


def test_git_push():
    pass


def test_git_staged_files():
    pass


def test_git_tag():
    pass


def test_git_update():
    pass


def test_is_node_package():
    pass


def test_is_python_package():
    pass


def test_make_changelog():
    pass


def test_read_file():
    version = "0.1.0"
    variable = "__version__"
    content = "{} = \"{}\"".format(variable, version)

    # create the tmpfile
    tmp = tempfile.NamedTemporaryFile()
    with open(tmp.name, "w") as f:
        f.write(content)

    # test
    assert read_file(tmp.name, variable) == version
    assert read_file(tmp.name) == content

    # close the file.
    tmp.close()


def test_release_package():
    pass


def test_replace_line():
    version_1 = "0.1.0"
    version_2 = "0.1.1"
    variable = "__version__"
    prepended = [
        "# This is a comment.\n",
        "# This is a second comment.\n",
        "# This is a third comment.\n",
    ]
    line = "{} = \"{}\""
    line_1 = line.format(variable, version_1)
    line_2 = line.format(variable, version_2)
    version_pattern = r"{} = ['\"][^'\"]*['\"]".format(variable)
    
    # create a temp file to load our content into.
    tmp = tempfile.NamedTemporaryFile()
    with open(tmp.name, "w") as f:
        f.write(line_1)
    
    # assert without prepended lines
    replace_line(tmp.name, version_pattern, line_2)
    assert read_file(tmp.name) == line_2
    assert read_file(tmp.name, variable) == version_2
    
    # assert with prepended items
    replace_line(tmp.name, version_pattern, line_1, prepended)
    with open(tmp.name) as f:
        lines = f.readlines()
        for l in lines:
            if l.strip() == line_1:
                count = -1
                total_prepended = len(prepended)
                for p in prepended:
                    count += 1
                    i = max(0, (lines.index(l) - (total_prepended - count)))
                    assert lines[i].strip() == p.strip()
    
    # close the file
    tmp.close()


def test_run():
    # Test when invoked with an invalid executable.
    with pytest.raises(AssertionError, match=r"Executable was not found. \(.+\)$"):
        run("non_existent_exec")

    # Test when invoked with a valid executable.
    assert run("echo example") == "example"


# Since this is just a fascade for replace_line, we don't need to test it.
def test_save_version():
    pass


def test_test_package():
    pass


def test_twine_upload():
    pass


def test_which():
    # Test with a valid executable
    assert which("sh") == "/bin/sh"
    # Test with an invalid executable.
    assert which("non_existant_exec_name") == None

