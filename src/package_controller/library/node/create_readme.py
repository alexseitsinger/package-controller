import os

from ..generic.run import run

COMMAND = "documentation build {input_file} -f {output_format} -o {output_file}"


def create_readme(input_path, output_name):
    root_dir = os.path.dirname(input_path)
    output_path = (os.path.join(root_dir, output_name),)
    run(
        COMMAND.format(
            input_file=input_path, output_format="md", output_file=output_path
        )
    )
    return output_path
