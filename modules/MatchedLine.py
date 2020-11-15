import re
import argparse


class MatchedLine:
    def __init__(self, line, line_num):
        self.line = line
        self.line_num = line_num
        self.patterns_pos = []

    def add_position(self, start):
        position = {'start': start}
        self.patterns_pos.append(position)

    # def print(self):
    #     for pos in self.patterns_pos:
    #         print(file_name + ":" + str(num_line) + ":" + '\033[44;33m{}\033[m'.format(match.group()))
