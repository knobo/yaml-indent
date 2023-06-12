""" A program to indent yaml files """
import argparse
import configparser
import os
import sys
from ruamel.yaml import YAML
from . import __version__

def find_config_file(dir_path):
    '''
    Searches for the configuration file (.yaml_indent.ini) in the
    given directory and its parent directories up to the home
    directory.

    Arguments:
    - dir_path (str): The directory path where to start the search for the configuration file.

    Returns:
    - str: The path to the configuration file if found, None otherwise.

    The function starts from the directory specified by dir_path and moves up towards the home directory.
    The search stops when it finds a configuration file or reaches the home directory.
    If the function cannot find a configuration file, it returns None.

    '''
    home_dir = os.path.expanduser("~")  # Home directory path
    while dir_path not in {home_dir, "/", ""}:  # Stop at the home directory
        config_path = os.path.join(dir_path, '.yaml_indent.ini')
        if os.path.exists(config_path):
            return config_path
        # Go up to the parent directory
        dir_path = os.path.dirname(dir_path)
    return None


def process_yaml_file(input_file, output_file=None, in_place=False):
    '''
    Reindents the YAML file(s) based on the specified configuration or default rules.
    
    Arguments:
    - input_file (str): The path to the input YAML file.
    - output_file (str, optional): The path to the output YAML file. If not provided, the output is printed to stdout.
    - in_place (bool, optional): If true, modifies the input file in place. Default is False.

    The function reads the configuration from a file found in the current directory or any parent directory,
    and applies it to reindent the input YAML file. The configuration file should be named '.yaml_indent.ini'.
    If no configuration file is found, default values are used.

    The default values for indentation are:
    - mapping: 2
    - sequence: 4
    - offset: 2
    '''
    yaml = YAML()
    yaml.explicit_start = True  # Start each document with '---'
    
    # Check for a configuration file
    config_path = find_config_file(os.path.dirname(input_file))
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
    with open(input_file, 'r', encoding='UTF-8') as stream:
        try:
            documents = list(yaml.load_all(stream))
        except Exception as exc:
            print(f"Error loading YAML data from {input_file}: {exc}")
            return

    # Open the output file and dump the data with correct indenting
    if in_place:
        with open(input_file, 'w', encoding='UTF-8') as outfile:
            try:
                for doc in documents:
                    yaml.dump(doc, outfile)
            except Exception as exc:
                print(f"Error writing YAML data to {input_file}: {exc}")
    elif output_file:
        with open(output_file, 'w', encoding='UTF-8') as outfile:
            try:
                for doc in documents:
                    yaml.dump(doc, outfile)
            except Exception as exc:
                print(f"Error writing YAML data to {output_file}: {exc}")
    else:
        try:
            for doc in documents:
                yaml.dump(doc, sys.stdout)
        except Exception as exc:
            print(f"Error writing YAML data to stdout: {exc}")

def main():
    '''Parse arguments and indent files'''

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", action="version", version=__version__)

    parser.add_argument(
        'input_file',
        help='The input YAML file to be indented'
    )
    parser.add_argument(
        '-o', '--output_file', nargs='?',
        default=argparse.SUPPRESS,
        help='The output file where the indented YAML will be written'
    )
    parser.add_argument('-i', '--in_place', action='store_true',
                        help='If set, the input file will be edited in place')
    args = parser.parse_args()

    process_yaml_file(
        args.input_file,
        getattr(args, 'output_file', None),
        args.in_place
    )


if __name__ == "__main__":
    main()
