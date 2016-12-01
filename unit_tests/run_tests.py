#!/usr/bin/python
# coding: utf8

import sys;
from tests.tests import *;

## TODO
# Usage ...
# Flags:
# -o: output
# -

FLAG_COLOR = 0x1;
FLAG_FULL = 0x2;

flags = 0;

for arg in sys.argv[1:]:
    if arg[0] == '-':
        if 'c' in arg:
            flags |= FLAG_COLOR;
        if 'f' in arg:
            flags |= FLAG_FULL;

test_length();
