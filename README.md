# Package Controller

## Description

A package that manages packages.

## Installation

```
pip install package_controller
```

## Usage

To run unit/integration tests.
```
pc test --unit | --integration
```

To add file(s) to a commit.
```
pc add -f <path> (-f <path> ...)
```

To create the commit.
```
pc commit -t <type> -s <subject> (-d <description>)
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

To release the latest version. (to PyPi and Github)
```
pc release
```

