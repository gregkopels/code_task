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
        file = 'index.html'
        url = "www.google.com"
        wget = os.system("wget " + url)

        # and then check the response...
        if os.path.isfile(file) == True:
            print("wget captured {}".format(url))
            assert 1 == 1
        else:
            print("wget did not capture {}".format(url))
            assert 1 == 0
