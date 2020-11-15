from modules import FileParser

import re
import argparse

log_message = 'messages'


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', help="Enter text to be searched")
    parser.add_argument('-c', '--color', dest='color', nargs='?', default=True, help="Colors output")
    parser.add_argument('-m', '--machine', dest='machine', nargs='?', default=True, help="Prints in JSON")
    args = parser.parse_args()

    f_parser = FileParser.FileParser(log_message, args.arg1)
    f_parser.parse()
    f_parser.print_matched_lines()


if __name__ == "__main__":
    main()






