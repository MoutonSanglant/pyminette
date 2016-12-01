# coding: utf8

import os;
import filecmp;
from subprocess import call;

PY = '../pyminette.py';
FLAGS = '-c';
PATH_RESULTS = 'test_results/';
PATH_TEST_CASES = 'test_cases/';
OUTPUT_FILE = 'result.out';

def compare_file(e, r):
    result = r.read();
    expect = e.read();
    if result != expect:
        print("\033[31m[-]\033[0m " + e.name);
        print('\033[33mexpected:\033[0m');
        print(expect);
        print('\033[33mreceived:\033[0m');
        print(result);
    else:
        print("\033[32m[+]\033[0m " + e.name);

def test_file(name):
    with open(OUTPUT_FILE, 'w+') as outfile:
        call([PY, FLAGS, PATH_TEST_CASES + name], stdout=outfile);
        outfile.seek(0);
        f = open(PATH_RESULTS + name, 'r');
        compare_file(f, outfile);
        outfile.close();
        f.close();

# Test files

def test_length():
    test_file('invalid_length');
    test_file('valid_length');
    os.remove(OUTPUT_FILE);

def test_comments():
    test_file('invalid_comment_bad_end1');
    test_file('invalid_comment_bad_end2');
    test_file('invalid_comment_bad_start1');
    test_file('invalid_comment_bad_start2');
    test_file('invalid_comment_nospace');
    test_file('invalid_comment_blank');
    test_file('invalid_comment_empty');
    test_file('valid_comment');
    os.remove(OUTPUT_FILE);

def full_test():
    test_length();
    os.remove(OUTPUT_FILE);
