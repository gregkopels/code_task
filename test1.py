import pytest
import sys
import subprocess
import os

iplist = '8.8.8.8'

class TestClass:

    def test_one(self):
        x = 'gregkopels@mail.com'
        assert 'greg' in x

    def test_two(self):
        hostname = "8.8.8.8"
        response = os.system("ping -c 1 " + hostname)
        # and then check the response...
        if response == 0:
            print("Ping is reachable to {}".format(hostname))
            assert 1 == 1
        else:
            print("Ping is not reachable to {}".format(hostname))
            assert 1 == 0


