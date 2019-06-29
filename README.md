# Package Controller

## Description

A CLI tool that acts as a wrapper for various other programs to make updating and publishing python and node packages easier.

## Installation

Preferred:
```
pipx install package-controller
```

Alternative:

```
pipenv install package-controller
```

Default:

```
pip install package-controller
```

## Usage

To stage and commit in one command:
```
pc save -t <type> -m <message> (<file>, <file>, <file>...)
```

To create new documentation for the package.
```
pc document
```

To pin the package versions for python or node.
```
pc pin --development | --production | --peer | --optional
```

To unpin the package versions for python or node.
```
pc unpin --development | --production | --peer | --optional
```

To get the diff of a file.
```
pc diff path/to/file
```

To run unit/integration tests.
```
pc test --unit --integration
```

To add file(s) to a commit.
```
pc add (<file>, <file>, ...)
```

To create the commit.
```
pc commit -t <type> -m <message>
```

To increase the major version
```
pc version --major (--no-git --force)
```

To increase the minor version
```
pc version --minor (--no-git --force)
```

To increase the patch version
```
pc version --patch (--no-git --force)
```

To get the current version
```
pc version
```

To build the current version.
```
pc build (--force)
```

To release the latest version. (to PyPi (Python) or NPM (Node), and git)
```
pc release (--remote <remote> --branch <branch> --no-tag --force)
```

