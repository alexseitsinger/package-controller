import json
from io import open
from ..generic.run import run
from ..generic.assert_which import assert_which
from ..python.is_python_package import is_python_package
from ..node.is_node_package import is_node_package
from ..generic.find_file import find_file
from ..generic.replace_line import replace_line


def unpin_versions_python(production, development):
    pass


def update_versions_node(json_dict, key):
    deps = json_dict.get(key, None)
    if deps is None:
        return
    for k, v in deps.items():
        version = v
        if not version.startswith("^"):
            version = "^{}".format(version)
        deps[k] = version


def unpin_versions_node(production, development, peer, optional):
    # Find the package file we're going to alter.
    package_file = find_file("package.json")

    # Get the original content from the package file
    original_content = None
    with open(package_file, "r") as f:
        # Read the JSON into a dictionary.
        original_content = json.loads(f.read())

    # If we didnt get the original content, there wa san error.
    if original_content is None:
        raise RuntimeError("Failed to read package file.")

    # Process the deps
    if production is True:
        update_versions_node(original_content, "dependencies")
    if development is True:
        update_versions_node(original_content, "devDependencies")
    if peer is True:
        update_versions_node(original_content, "peerDependencies")
    if optional is True:
        update_versions_node(original_content, "optionalDependencies")

    # Write the new content to the file.
    with open(package_file, "w") as f:
        f.write(json.dumps(original_content, indent=2, sort_keys=True))

    # Return a dictionary of each section that was pinned.
    return {
        "production": production,
        "development": development,
        "optional": optional,
        "peer": peer,
    }


def unpin_versions(production=False, development=False, optional=False, peer=False):
    is_python = is_python_package()
    is_node = is_node_package()
    if is_python and not is_node:
        return unpin_versions_python(production=production, development=development)
    elif is_node and not is_python:
        return unpin_versions_node(
            production=production, development=development, optional=optional, peer=peer
        )
    elif is_node and is_python:
        raise RuntimeError("Both python and node packages were detected.")
    else:
        raise RuntimeError("Neither python nor node package was detected.")
