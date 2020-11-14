import argparse
import os
import os.path
import re
import sys

file = 'messages'
pattern = 'error'
output_format = '-c'

def check_logs(log_file):
    num_line = 0
    start_pos = ""
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', help="Enter the text to find in log")
    args = parser.parse_args()
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

    def get_args():
        parser = argparse.ArgumentParser()
        parser.add_argument('arg1', help="Enter the text to find in log")
        args = parser.parse_args()

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', help="Enter the text to find in log")
    args = parser.parse_args()


def main():
    get_arguments
    log_file = check_logs('messages')



if __name__ == "__main__":
    main()