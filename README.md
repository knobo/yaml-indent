# YAML Indent
## Overview

yaml-indent is a Python utility for formatting YAML files with correct
indentation. It reads in a YAML file, processes it, and outputs a new
YAML file with proper indentation, making the file more readable and
manageable.

## How it Works

The utility makes use of the PyYAML library to parse the input YAML
file, and re-dumps the YAML data into the output file with correct
indentation.

## Installation

To use this utility, you must have Python 3 installed on your
system. Additionally, you need to install the PyYAML library. You can
install it using pip:

``` sh
pip install yaml-indent
```

You can then clone this repository to your local machine.

## Usage

To use this utility, you need to run the Python script yaml_indent.py
with two arguments: the input YAML file and the output YAML file. 

Here is an example:

``` sh
python input.yaml output.yaml
```

In this command, input.yaml is the YAML file you want to format and
output.yaml is the file where the formatted YAML will be written. If
output.yaml already exists, it will be overwritten.

## Contributing

Contributions to this project are welcome. If you find a bug or think
of a feature that this utility could benefit from, please open an
issue or submit a pull request.

## License

This project is open source under the terms of the GPL License.

