# coding: utf8

import os;
import filecmp;
from subprocess import call;

def compare_file(filename, res):
    f = open('results/' + filename, 'r');
    exp = f.read();
    if res != exp:
        print("\033[31m[-]\033[0m " + filename);
        print('expected:');
        print(exp);
        print('received:');
        print(res);
    else:
        print("\033[32m[+]\033[0m " + filename);

def test_file(filename):
    with open('tmp', 'w+') as outfile:
        call(['../pyminette.py', 'inputs/' + filename + '.c'], stdout=outfile);
        outfile.seek(0);
        compare_file(filename, outfile.read());
        os.remove('tmp');

def test_length():
    test_file('valid_length');
    test_file('invalid_length');

def full_test():
    test_length();
