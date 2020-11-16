#!/usr/bin/env python

"""
__author__      = "Greg Kopels"
This class imports matches MatchedLine to parsed a file with using an argument in the command line.
python3 find_matched_lines.py <file name> <pattern to find> <optional argument>

For example
python3 find_matched_lines.py error (will print only file name and line)
python3 find_matched_lines.py error -c (will print the pattern in blue)
python3 find_matched_lines.py error -m (will print the output in JSON)
"""

import re
import os
from modules import MatchedLine
import yaml

file = 'messages'


class FileParser:
    def __init__(self, file, pattern, output_format):
        self.file = file
        self.pattern = pattern
        self.matched_lines = []
        self.output_format = output_format

    def parse(self):
        line_num = 1
        # Verify the file exist
        if os.path.isfile(self.file):
            with open(self.file, 'r') as f:
                lines = f.readlines()
                # Read lines in file searching for pattern using re
                for line in lines:
                    matches = re.finditer(self.pattern, line)
                    matched_line = MatchedLine.MatchedLine(line, line_num)
                    # Locate the matched line and starting position in the line
                    for match in matches:
                        start_position = match.start()
                        matched_line.add_position(start_position)
                        self.matched_lines.append(matched_line)
                    line_num += 1
        else:
            print('File cannot be found')

    def print_standard(self):
        # Print output depends on the arguments used in the commmand
        # Standard = no arg
        for match_line in self.matched_lines:
            print(self.file, match_line.line_num)

    def print_color(self):
        # Print output for color =  -c/--color
        for match_line in self.matched_lines:
            print(self.file, match_line.line_num, '\033[44;33m{}\033[m'.format(match_line.line))

    def print_machine(self):
        # Print output for machine = -m/--machine
        for match_line in self.matched_lines:
            temp_handler = str([self.file, match_line.line_num, self.get_positions(match_line.patterns_pos),self.pattern])
            #yaml_temp = {'File_Name': temp_handler[0], 'Line_num': temp_handler[1], 'Start_pos': temp_handler[2]}
            yaml_out = yaml.dump(temp_handler, explicit_start=True, default_flow_style=False)
            print(yaml_out)
            #print(file, match_line.line_num, self.get_positions(match_line.patterns_pos))

    def print_matched_lines(self):
        # Separates the print output according to argument from command line
        if self.output_format == 'standard':
            self.print_standard()
        elif self.output_format == 'color':
            self.print_color()
        elif self.output_format == 'machine':
            self.print_machine()

    def get_positions(self, positions):
        # Locates the starting position for occurrence in the line
        pos_str = ''
        for pos in positions:
            pos_str = pos_str + str(pos['start']) + ' '
        return pos_str



