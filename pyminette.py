#!/usr/bin/python
# coding: utf8

from tools.parser import test_line_length, disableColor, color;
from tools.comment import check_comment;
import os, sys


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
        errors += analyse(l_number, line);
        l_number +=1 ;
    if (not errors):
        print (color.colorSet.OKGREEN + "Il semblerait fort que ce fichier soit tout parfait, bravo !" + color.colorSet.EOC);
    else:
        print (color.colorSet.WARNING + "Il y a en tout (au moins) %i erreur%s ! Espèce de gros boulet va !" %(errors, "s" if (errors > 1) else "") + color.colorSet.EOC);
