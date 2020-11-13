import pytest
import sys
import subprocess
import pexpect
import os

class TestClass:
    def test_one(self):
        child = pexpect.spawn()
        child.sendline('ip a show eth0')
        child.expect(#)

    # def test_two(self):
    #     file = 'index.html'
    #     url = "www.google.com"
    #     wget = os.system("wget " + url