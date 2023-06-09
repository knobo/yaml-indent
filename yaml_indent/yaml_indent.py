#!/usr/bin/env python3

import argparse
import configparser
import os
from ruamel.yaml import YAML
import sys

def find_config_file():
    # Start from the current directory
    dir_path = os.getcwd()
    home_dir = os.path.expanduser("~")  # Home directory path
    while dir_path != home_dir:  # Stop at the home directory
        config_path = os.path.join(dir_path, '.yaml_indent.ini')
        if os.path.exists(config_path):
            return config_path
        # Go up to the parent directory
        dir_path = os.path.dirname(dir_path)
    return None

def process_yaml_file(input_file, output_file=None, in_place=False):
    yaml = YAML()

    # Check for a configuration file
    config_path = find_config_file()
    if config_path:
        config = configparser.ConfigParser()
        config.read(config_path)
        # Get the mapping, sequence, and offset values from the config file
        mapping = config.getint('YAML', 'mapping', fallback=2)
        sequence = config.getint('YAML', 'sequence', fallback=4)
        offset = config.getint('YAML', 'offset', fallback=2)
    else:
        mapping, sequence, offset = 2, 4, 2  # Default values

    yaml.indent(mapping=mapping, sequence=sequence, offset=offset)

    # Open the input YAML file and load the data
    with open(input_file, 'r') as stream:
        try:
            data = yaml.load(stream)
        except Exception as exc:
            print(exc)
    
    # Open the output file and dump the data with correct indenting
    if in_place:
        with open(input_file, 'w') as outfile:
            try:
                yaml.dump(data, outfile)
            except Exception as exc:
                print(exc)
    elif output_file:
        with open(output_file, 'w') as outfile:
            try:
                yaml.dump(data, outfile)
            except Exception as exc:
                print(exc)
    else:
        try:
            yaml.dump(data, sys.stdout)
        except Exception as exc:
            print(exc)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='The input YAML file to be indented')
    parser.add_argument('-o', '--output_file', nargs='?', default=argparse.SUPPRESS,
                        help='The output file where the indented YAML will be written')
    parser.add_argument('-i', '--in_place', action='store_true',
                        help='If set, the input file will be edited in place')
    args = parser.parse_args()
    
    process_yaml_file(args.input_file, getattr(args, 'output_file', None), args.in_place)

if __name__ == "__main__":
    main()
