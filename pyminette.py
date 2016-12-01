#!/usr/bin/python

import os, sys

for file in sys.argv[1:]:
    f = open(file, 'r');
    lines = f.read().split('\n');
    for line in lines:
        print (line);

print ('ok');
