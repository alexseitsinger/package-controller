import subprocess
import shlex

from .assert_which import assert_which


def run(cmd, raise_exception=True):
    args = cmd
    if isinstance(args, str):
        args = shlex.split(args)
    assert_which(args[0])
    process = subprocess.run(args, capture_output=True)
    out = process.stdout.strip().decode("utf-8")
    err = process.stderr.strip().decode("utf-8")
    if process.returncode != 0:
        # We need to not raise an exception when we encounter one with pytest.
        # We also need to return the stdout, instead of stderr, if we encounter
        # an exception with pytest.
        if raise_exception is True:
            raise RuntimeError(err)
    return out
