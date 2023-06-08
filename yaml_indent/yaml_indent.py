#!/usr/bin/env python3

import argparse
import yaml

def process_yaml_file(input_file, output_file):
    # Open the input YAML file and load the data
    with open(input_file, 'r') as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    # Open the output file and dump the data with correct indenting
    with open(output_file, 'w') as outfile:
        try:
            yaml.safe_dump(data, outfile, default_flow_style=False, sort_keys=False)
        except yaml.YAMLError as exc:
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
