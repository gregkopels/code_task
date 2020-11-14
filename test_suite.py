import device
from device import device
import paramiko
import subprocess
import re
import os
import pytest

ip = 'ec2-52-29-106-153.eu-central-1.compute.amazonaws.com'
commands = 'ls -ltr\n'
pkey_default = paramiko.RSAKey.from_private_key_file('linux-1-key.pem')
server_info = {'hostname': ip, 'port': '22', 'username': 'ec2-user', 'pkey': pkey_default}

class TestClass:

    def test_one(self):
        ping_reply = subprocess.call('ping %s -c 2' % (ip), shell=True)
        if ping_reply == 0:
            print('IP is reachable')
            assert True
        else:
            print('The Server is not reachable')

    def test_two(self):
        server = device(**server_info)
        server.connect()
        if server.client.get_transport() == True:
            assert 1 == 1
            print('SSH connection was successful')
        else:
            print('SSH connection was NOT successful')

    def test_three(self):
        file = 'ports.txt'
        os.system('nmap google.com > ports.txt')

        with open(file) as f:
            lines = f.readlines()

            for line in lines:
                http = re.search('80/tcp  open', line)
                https = re.search('443/tcp open', line)
                if http == True and https == True:
                    print('Both ports are open')
                    assert True
                else:
                    print('Both ports are not open')