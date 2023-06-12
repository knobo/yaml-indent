# YAML Indent

`yaml-indent` is a Python script to re-indent YAML files according to configurable or default indentation rules. It uses the `ruamel.yaml` library for parsing and writing YAML.

## Installation

The script requires Python 3.

``` sh
pip install yaml-indent
```

## Usage

You can run `yaml-indent` from the command line with the following syntax:

``` sh
yaml-indent <input_file> [-o <output_file>] [-i]
```

Where:

- `<input_file>` is the path to the input YAML file to be re-indented.
- `-o <output_file>` (optional) is the path to the output file where the indented YAML will be written.
- `-i` (optional) if set, the input file will be edited in place.

If no output file is specified and `-i` is not set, the indented YAML will be printed to the standard output.

## Configuration

`yaml-indent` looks for a `.yaml_indent.ini` configuration file in the
the yaml files directory and all parent directories up to the home
directory. The configuration file should be in the INI format and can
specify the `mapping`, `sequence`, and `offset` indentation values
under the `YAML` section.

Here's an example:

```ini
[YAML]
mapping=4
sequence=4
offset=0
```
## Contributing

Contributions to this project are welcome. If you find a bug or think
of a feature that this utility could benefit from, please open an
issue or submit a pull request.

## Source Code

The source code for this project is hosted on GitHub. You can access
it at [https://github.com/knobo/yaml-indent](https://github.com/knobo/yaml-indent).

## License

This project is open source under the terms of the GPL License.

