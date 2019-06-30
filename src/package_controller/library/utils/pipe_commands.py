from subprocess import Popen, PIPE
import shlex


def pipe_commands(commands):
    first_proc = None
    last_proc = None
    for command in commands:
        args = shlex.split(command)
        if first_proc is None:
            first_proc = last_proc = Popen(args, stdout=PIPE, stderr=PIPE)
        else:
            last_proc = Popen(args, stdin=last_proc.stdout, stdout=PIPE, stderr=PIPE)
    first_proc.stdout.close()
    out, err = last_proc.communicate()
    decoded = out.decode("utf-8")
    return decoded
