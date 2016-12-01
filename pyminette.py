#!/usr/bin/python
from tools.parser import *
import os, sys

#print(rep);
#sys.stdout = open(output, 'w');

class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    EOC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def test_space(line):
    print("test_space on: %s" %(line));

def test_comment(line):
    print("test_comment on: %s" %(line));

def test_line_length(l_number, line):
    c = 0;
    for char in line:
        if (char == '\t'):
            c += (4 - c%4);
        else:
            c += 1;
    if (c > 80):
        print (color.FAIL + "L%i -> Cette ligne excède 80 caractères: %i caractères trouvés !" %(l_number, c) + color.EOC + "\n" + line);
        return (1);
    return (0);

#tab = [test_space, test_comment, comment];
tab = [test_line_length];
def analyse(i, line):
    errors = 0;
    for fn in tab:
        errors += fn(i, line);
    return (errors);

for file in sys.argv[1:]:
    f = open(file, 'r');
    lines = f.read().split('\n');
    l_number = 1;
    errors = 0;
    for line in lines:
        #check_comment(line);
        errors += analyse(l_number, line);
        l_number +=1 ;
    if (not errors):
        print (color.OKGREEN + "Il semblerait fort que ce fichier soit tout parfait, bravo !" + color.EOC);
    else:
        print (color.WARNING + "Il y a en tout (au moins) %i erreur%s ! Espèce de gros boulet va !" %(errors, "s" if (errors > 1) else "") + color.EOC);
#print("Etat du tableau de fonctions :",tab);
#print("size=%i" %(len(tab)));

str1 = "banane"
str2 = "banane"
if (str1 == str2):
    print("identiques");