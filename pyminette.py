#!/usr/bin/python
import os, sys
from tools.parser import *

def test_space(line):
    print("test_space on: %s" %(line));

def test_comment(line):
    print("test_comment on: %s" %(line));

tab = [test_space, test_comment, comment];
def analyse(line):
    for fn in tab:
        fn(line);

for file in sys.argv[1:]:
    f = open(file, 'r');
    lines = f.read().split('\n');
    for line in lines:
        analyse(line);
print ('ok');

print("Etat du tableau de fonctions :",tab);
print("size=%i" %(len(tab)));
