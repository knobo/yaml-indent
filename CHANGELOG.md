# Changes

## [0.1.4] - 2023-06-11
- Allow multiple documents in one file

## [0.1.3] - 2023-06-11
- Fix for running outside homedir and missing config file
- Added -v for printing version info

## [0.1.2] - 2023-06-11

### Changed
- Update documentation
- This CHANGELOG.md file.
- Start searching for config file starting from the yaml-files directory

## [0.1.1] - 2023-06-09

### Changed
- Replaced `pyyaml` library with `ruamel.yaml`.
- Support for configuration files named `.yaml_indent.ini` in the current directory and all parent directories up to the home directory.
- The `-i` command line option to edit files in place.
- Added some URLs to pyproject.toml

## [0.1.0] - 2023-06-08

### Added
- Initial release of `yaml-indent`.
- Support for re-indenting YAML files with a default indentation of 2 spaces.
