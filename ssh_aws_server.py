import device
from modules import Device
import paramiko
import pytest

ip = 'ec2-52-29-106-153.eu-central-1.compute.amazonaws.com'
commands = 'ls -ltr\n'
pkey_default = paramiko.RSAKey.from_private_key_file('linux-1-key.pem')
server_info = {'hostname': ip, 'port': '22', 'username': 'ec2-user', 'pkey': pkey_default}

def main():
    server = Device(**server_info)
    server.connect()
    commands_output = server.send_command('date')
    print(commands_output)

    if server.client.get_transport() == True:
        assert 1 == 1


if __name__ == '__main__':
    main()