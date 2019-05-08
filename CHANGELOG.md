# Changelog


## [Unreleased]

### New Features
- renamed exceptions, added new one for util
- added new util methods



### Refactoring
- changed package_setup.py to attempt to use name provided, then fallback to name of package directory




### Administration and Chores
- deleting __version__.py module and put __version__ variable in __init__.py instead.
- removed duplicate installation of local package, re-installed it to dev packages
- added setup_utils.py module to package root
- updated settings, fixed typos etc.
- added changelog




## v0.1.1 (2019-05-05)






### Administration and Chores
- replaced setuptools setup() with our custom package_setup() script
- updated version




## v0.1.0 (2019-05-03)









