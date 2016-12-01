# coding: utf8

import os;
import filecmp;
from subprocess import call;

def compare_file(filename, res):
    f = open('results/' + filename, 'r');
    exp = f.read();
    if res != exp:
        print("\033[31m[-]\033[0m " + filename);
        print('\033[33mexpected:\033[0m');
        print(exp);
        print('\033[33mreceived:\033[0m');
        print(res);
    else:
        print("\033[32m[+]\033[0m " + filename);

def test_file(filename):
    with open('tmp', 'w+') as outfile:
        call(['../pyminette.py', '-c', 'inputs/' + filename + '.c'], stdout=outfile);
        outfile.seek(0);
        compare_file(filename, outfile.read());
        os.remove('tmp');

def test_length():
    test_file('invalid_length');
    test_file('valid_length');

def test_comments():
    test_file('invalid_comment_bad_end1');
    test_file('invalid_comment_bad_end2');
    test_file('invalid_comment_bad_start1');
    test_file('invalid_comment_bad_start2');
    test_file('invalid_comment_nospace');
    test_file('invalid_comment_blank');
    test_file('invalid_comment_empty');
    test_file('valid_comment');

def full_test():
    test_length();
