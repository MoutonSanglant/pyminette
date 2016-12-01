
import filecmp;
from subprocess import call;

def compare_file(filename, res):
    f = open('tests/results/' + filename, 'r');
    exp = f.read();
    if cmp(res, exp):
        print("\033[31m[-]\033[0m " + filename);
        print('expected:');
        print(exp);
        print('received:');
        print(res);
    else:
        print("\033[32m[+]\033[0m " + filename);
    

def test_file(filename):
    with open('tmp', 'r+') as outfile:
#        print('inputs/' + filename + '.c');
#        quit();
        call(['../pyminette.py', 'tests/inputs/' + filename + '.c'], stdout=outfile);
        outfile.seek(0);
        compare_file(filename, outfile.read());
#        print(outfile.read());

def test_length():
    test_file('valid_length');
    test_file('invalid_length');
