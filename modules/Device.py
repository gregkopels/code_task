
import paramiko
import time


class Device:
    def __init__(self, hostname, port, username, pkey, *args):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.client = paramiko.SSHClient()
        self.pkey = pkey
        self.shell = None

    def connect(self):
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=self.hostname, port=self.port, username=self.username,
                            pkey=self.pkey, look_for_keys=False, allow_agent=False)
        print(f'Connected to {self.hostname}')

    def start_shell(self):
        self.shell = self.client.invoke_shell()
        #self.shell.recv(10000)

    def send_command(self, command, timeout=1):
        print(f'Sending command to {command}')
        self.start_shell()
        self.shell.send(command + '\n')
        time.sleep(timeout)
        output = self.get_shell_output()
        return output

    def get_shell_output(self, n=100000):
        output = self.shell.recv(n)
        return output.decode()