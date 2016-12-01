#!/usr/bin/python
# coding: utf8

from i18n.locale import msg, setLang, disableColor;

#from tools.color import disableColor;
from tools.parser import test_line_length;
from tools.comment import check_comment;

import os, sys

setLang("fr");

FLAG_COLOR = 0x1;
FLAG_FULL = 0x2;

flags = 0;
flag_count = 0;
for arg in sys.argv[1:]:
    if arg[0] == '-':
        flag_count += 1;
        if 'c' in arg:
            flags |= FLAG_COLOR;
            disableColor();
        if 'f' in arg:
            flags |= FLAG_FULL;
        if 'n' in arg:
            setLang("nm");

tab = [test_line_length, check_comment];
def analyse(i, line):
    errors = 0;
    for fn in tab:
        errors += fn(i, line);
    return (errors);

for file in sys.argv[1 + flag_count:]:
    f = open(file, 'r');
    lines = f.read().split('\n');
    l_number = 1;
    errors = 0;
    for line in lines:
        if l_number > 11:
            errors += analyse(l_number, line);
        l_number +=1 ;
    if (not errors):
        print(msg.ok_file());
        #print (msg["ok_file"]);
    else:
        print(msg.err_file() % (errors, "s" if (errors > 1) else ""));
        #print (msg["err_file"] % (errors, "s" if (errors > 1) else ""));