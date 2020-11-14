import re
import argparse

class file_parser:
    def __init__(self, file, pattern):
        self.file = file
        self.pattern = pattern
        self.matched_lines = []

    def parse(self):
        if os.path.isfile(log_file) == True:
            with open(log_file, 'r') as f:
                lines = f.readlines()
            for line in lines:
                match = re.search(args.arg1, line)
                num_line += 1
                if match:
                    print(file_name + ":" + str(num_line) + ":" + '\033[44;33m{}\033[m'.format(match.group()))
            else:
                if match != args.arg1:
                    print('\033[44;33m{}\033[m'.format(args.arg1) + ' Was not found')

        else:
            print("\n* File {} doesnt exist : (Please check and try again.)\n".format(log_file))
            sys.exit()
