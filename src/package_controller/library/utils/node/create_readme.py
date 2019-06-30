import os

from ..run import run

COMMAND = "documentation build {input_file} -f {output_format} -o {output_file} --markdown-toc false"


def create_readme(root_dir, input_path, output_name):
    output_path = os.path.join(root_dir, output_name)
    run(
        COMMAND.format(
            input_file=input_path, output_format="md", output_file=output_path
        )
    )
    return output_path
