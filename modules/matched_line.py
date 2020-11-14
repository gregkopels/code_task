import re
import argparse

class matched_line:
    def __init__(self, line, line_num):
        self.line = line
        self.line_num = line_num
        self.patterns_pos = []

    def add_position(self, position):
        self.patterns_pos.append(position)