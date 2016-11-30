#!/usr/bin/python
#Ceci est un commentaire
""" un gros
commenire
multipline """

def vache():
	print("remuuuh");
	print("testA"); print("testB");

def inc(i):
	i = i+1;
	i += 1;
	j = 7;
	return (i, j);

print("hello");
print("meuhhhhh");
vache();
vache();

a,b = 3,7;

print(a);
print(b,a);

m, n = inc(a);
print(m);
print(n);

print(20/3);
z = 20/3;
print(z);

def sub_div(z):
	z /= 2;
	z **= 2;
	return (z);

print(sub_div(z));

T = "banane" * 2 + "toto" * 3;
print(T);

z = 4;
print(z);
if (z == 2):
	print("egal a 2");
elif (z == 4):
	print("egal à 4");
else:
	print("grrrrr");

print("test %s = %i" %("les carotes sont cuites",z));
tab = [3,4,5,6,7] * 3;
tab2 = [7, 9, 0, -3] *2;
tab[0] += 1;
tab += tab2;
print(tab);
print(len(tab));
print(tab.count(7));
print(tab.index(7));
print(tab[7:10]);

str = "les carotes sont cuites";

import os
os.system('ls -l');

from subprocess import call
call(["ls","-l"])

call(["echo","banane"]);
call(["echo",str]);
print(type(z));
x=3
y=2
if ((x==3 and y==2) and x==1):
	print("YEEH");
if (x==3 or y==2):
	print("YESYESSS");
i = 4000000000;
i *= 1000;
print(i);
print(type(i));

i = 0x04;
print(i);
i = 0b110;
print(i);
i = 0x06;
if (i & 0x04):
	print("0x04");
if (i & 0x02):
	print("0x02");

from enum import Enum
class MASKS(Enum):
	N_MASK = 0x00;
	L_MASK = 0x01;
	H_MASK = 0x02;

i = MASKS.N_MASK;
print(type(i));

prenom = input('Entrez votre prénom (entre guillemets) : ');
print ("Bonjour", prenom);


from math import sqrt,sin
print(sqrt(16));
print(sin(67));
