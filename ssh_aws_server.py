#!/usr/bin/env python
"""
__author__      = "Greg Kopels"
This script using class Device.py to test connectivity to an AWS server. It be run as followed:
docker run -it --rm --privileged -v `pwd`:`pwd` -w `pwd` tester python3 ssh_aws_server.py
docker run -it --rm --privileged -v `pwd`:`pwd` -w `pwd` tester pytest ssh_aws_server.py
"""
from modules import Device
import paramiko
import pytest

ip = 'ec2-52-29-106-153.eu-central-1.compute.amazonaws.com'
commands = 'ls -ltr\n'
pkey_default = paramiko.RSAKey.from_private_key_file('linux-1-key.pem')
server_info = {'hostname': ip, 'port': '22', 'username': 'ec2-user', 'pkey': pkey_default}


def main():
    server = Device.Device(**server_info)
    server.connect()
    commands_output = server.send_command('date')
    print(commands_output)

    if server.client.get_transport() == True:
        assert 1 == 1


if __name__ == '__main__':
    main()