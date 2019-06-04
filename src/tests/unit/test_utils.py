import pytest
import tempfile

from package_controller.utils.assert_commit import assert_commit
from package_controller.utils.assert_commit_type import assert_commit_type
from package_controller.utils.assert_status import assert_status
from package_controller.utils.build_package import build_package
from package_controller.utils.bump_version import bump_version
from package_controller.utils.find_file import find_file
from package_controller.utils.find_init_module import find_init_module
from package_controller.utils.format_commit_description import \
    format_commit_description
from package_controller.utils.format_commit_text import \
    format_commit_text
from package_controller.utils.get_version import get_version
from package_controller.utils.git_add import git_add
from package_controller.utils.git_add_file import git_add_file
from package_controller.utils.git_commit import git_commit
from package_controller.utils.git_push import git_push
from package_controller.utils.git_staged_files import git_staged_files
from package_controller.utils.git_tag import git_tag
from package_controller.utils.git_update import git_update
from package_controller.utils.is_node_package import is_node_package
from package_controller.utils.is_python_package import is_python_package
from package_controller.utils.make_changelog import make_changelog
from package_controller.utils.read_file import read_file
from package_controller.utils.release_package import release_package
from package_controller.utils.replace_line import replace_line
from package_controller.utils.run import run
from package_controller.utils.save_version import save_version
from package_controller.utils.twine_upload import twine_upload
from package_controller.utils.which import which
from package_controller.utils.assert_which import assert_which



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

