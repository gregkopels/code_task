import re
import subprocess
import os

interfaces = os.system('ifconfig > ifconfig.txt')

if_config = 'ifconfig.txt'

with open(if_config) as f:
    num_line = 0
    lines = f.readlines()
    for line in lines:
        match = re.search('eth0', line)
        num_line += 1
        if match:
            print(if_config + ":" + str(num_line) + ":" + '\033[44;33m{}\033[m'.format(match.group()))

        # else:
        #     if match != args.arg1:
        #         print('\033[44;33m{}\033[m'.format('eth0') + ' Was not found')


