#!/bin/sh
docker run -it --rm --cap-add=NET_ADMIN --privileged -v `pwd`:`pwd` -w `pwd` tester pytest test_suite.py