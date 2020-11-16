"""
__author__      = "Greg Kopels"
This class matches line, line number, line position and color of patter in output. It is imported into
FileParser.py.
"""


class MatchedLine:
    def __init__(self, line, line_num):
        self.line = line
        self.line_num = line_num
        self.patterns_pos = []
        self.color_pos = []

    def add_position(self, start):
        position = {'start': start}
        self.patterns_pos.append(position)

    def color_position(self, start, end):
        position = {'start': start, 'end': end}
        self.color_pos.append(position)

