import argparse
import os
import os.path
import re
import sys
import json
import datetime

def check_logs(log_file):
    num_line = 0
    file_name = 'messages'
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', help="Enter text to be searched")
    parser.add_argument('-c', '--color', dest='color', nargs='?', default=True, help="Colors output")
    parser.add_argument('-m', '--machine', dest='machine', nargs='?', default=True, help="Prints in JSON")
    args = parser.parse_args()
    if os.path.isfile(log_file) == True:
        with open(log_file, 'r') as f:
            lines = f.readlines()
        for line in lines:
            match = re.search(args.arg1, line)
            num_line += 1
            if args.color is None:
                print('hi')
            if args.machine is None:
                print('bye')
                dict = match
                dict
                with open('temp_json', 'w') as fout:

                    json.dump(match, fout)
                #print(json.dump(match, ensure_ascii=b))
                #print(file_name + ":" + str(num_line) + ":" + '\033[44;33m{}\033[m'.format(match))
            else:
                print(file_name, str(num_line))
                    #print(file_name + ":" + str(num_line) + ":" + '\033[44;33m{}\033[m'.format(match.group()))

    # else:
    #     print("\n* File {} doesnt exist : (Please check and try again.)\n".format(log_file))
    #     sys.exit()


def main():
    check_logs('messages')


if __name__ == "__main__":
    main()
