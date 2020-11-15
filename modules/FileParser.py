import re
import sys
import os
from modules import MatchedLine
import json
import argparse

file = 'messages'


class FileParser:
    def __init__(self, file, pattern):
        self.file = file
        self.pattern = pattern
        self.matched_lines = []
        #self.args = None

    def get_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('arg1', help="Enter the text to find in log")
        args = parser.parse_args(self)
        return args

    def parse(self):
        line_num = 1
        if os.path.isfile(self.file):
            with open(self.file, 'r') as f:
                lines = f.readlines()
                # go over lines in file
                for line in lines:
                    matches = re.finditer(self.pattern, line)
                    matched_line = MatchedLine.MatchedLine(line, line_num)
                    for match in matches:
                        start_position = match.start()
                        matched_line.add_position(start_position)
                        self.matched_lines.append(matched_line)
                    line_num += 1
        else:
            print('File cannot be found')

    def print_matched_lines(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('arg1', help="Enter text to be searched")
        parser.add_argument('-c', '--color', dest='color', nargs='?', default=True, help="Colors output")
        parser.add_argument('-m', '--machine', dest='machine', nargs='?', default=True, help="Prints in JSON")
        args = parser.parse_args()

        for matched_line in self.matched_lines:
            dict = matched_line.patterns_pos
            with open('temp_json', 'w') as fout:
                json.dump(matched_line.patterns_pos, fout)

            with open('temp_json', 'r') as temp_read:
                machine_read = json.load(temp_read)
                #print(machine_read)

                for postion in range(len(dict)):
                    if args.color is None:
                        # Print wih argument --color
                        print('hi')
                        print(file, matched_line.line_num, '\033[44;33m{}\033[m'.format(self.pattern))
                    if args.machine is None:
                        # Print wih argument --machine to JSON
                        print(machine_read)
                        print('bye')
                    else:
                        # Print with no argument
                        print(file, matched_line.line_num)
            #
            # for postion in range(len(dict)):
            #     if args.color is None:
            #         # Print wih argument --color
            #         print('hi')
            #         print(file, matched_line.line_num, '\033[44;33m{}\033[m'.format(self.pattern))
            #     if args.machine is None:
            #         # Print wih argument --machine to JSON
            #         print('bye')
            #     else:
            #         # Print with no argument
            #         print(file, matched_line.line_num)

