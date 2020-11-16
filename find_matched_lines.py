#!/usr/bin/env python

"""
__author__      = "Greg Kopels"
This script using class FileParser.py to match a pattern given in the command line.

For example
python3 find_matched_lines.py <file> <pattern> <optional arguments>
python3 find_matched_lines.py error (will print only file name and line)
python3 find_matched_lines.py error -c (will print the pattern in blue)
python3 find_matched_lines.py error -m (will print the output in YAML)
"""

from modules import FileParser
import argparse


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', help="File name")
    parser.add_argument('arg2', help="Enter text to be searched")
    parser.add_argument('-c', '--color', dest='color',  nargs='?', default=True, help="Colors output")
    parser.add_argument('-m', '--machine', dest='machine',  nargs='?', default=True, help="Prints in JSON")
    args = parser.parse_args()
    file = args.arg1
    pattern = args.arg2
    if args.color is not True:
        output_format = 'color'
    elif args.machine is not True:
        output_format = 'machine'
    else:
        output_format = 'standard'
    f_parser = FileParser.FileParser(file, pattern, output_format)
    f_parser.parse()
    f_parser.print_matched_lines()


if __name__ == "__main__":
    main()






