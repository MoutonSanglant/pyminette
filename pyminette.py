#!/usr/bin/python

import os, sys

for file in sys.argv:
    f = open(file, 'r');
    list = f.read().split('\n');
    for x in list:
        print x;
