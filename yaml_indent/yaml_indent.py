#!/usr/bin/env python3

import argparse
import configparser
import os
from ruamel.yaml import YAML



def find_config_file():
    # Start from the current directory
    dir_path = os.getcwd()
    while dir_path != os.path.dirname(dir_path):  # Stop at the root directory
        config_path = os.path.join(dir_path, 'config.ini')
        if os.path.exists(config_path):
            return config_path
        # Go up to the parent directory
        dir_path = os.path.dirname(dir_path)
    return None



def process_yaml_file(input_file, output_file):
    yaml = YAML()
    # Open the input YAML file and load the data
    with open(input_file, 'r') as stream:
        try:
            data = yaml.load(stream)
        except Exception as exc:
            print(exc)


    config_path = find_config_file()
    if config_path:
        config = configparser.ConfigParser()
        config.read(config_path)

        mapping = config.getint('YAML', 'mapping', fallback=2)
        sequence = config.getint('YAML', 'sequence', fallback=4)
        offset = config.getint('YAML', 'offset', fallback=2)
    else:
        mapping, sequence, offset = 2, 4, 2  # Default values

    yaml.indent(mapping=mapping, sequence=sequence, offset=offset)

    with open(output_file, 'w') as outfile:
        try:
            yaml.dump(data, outfile)
        except Exception as exc:
            print(exc)



def main():
    parser = argparse.ArgumentParser(description="Read a YAML file and write it out with correct indentation")

    # Add the arguments
    parser.add_argument("InputFile", metavar="inputfile", type=str, help="the input YAML file")
    parser.add_argument("OutputFile", metavar="outputfile", type=str, help="the output YAML file")

    # Execute the parse_args() method
    args = parser.parse_args()

    process_yaml_file(args.InputFile, args.OutputFile)
    
            
if __name__ == "__main__":
    # Create the parser
    main()
