# coding: utf8
import re

b1 = re.compile("\A/\*\Z");					# debut de commentaire bien placé au début de la ligne.
b2 = re.compile("/\*");						# symbole du début de commentaire ignorant son placement.
def open_comment(n, line):
    if (b2.search(line)):
        v.i += 1;
        v.fn_entry = 1;
        if (b1.search(line)):
            return (0);
        else:
            return (1);
    return (0);

c1 = re.compile("\A\*\*([\\t ])");			# partie médiane d'un commentaire qui contient obligatoirement un espace ou une tab ensuite.
def current_comment(n, line):
    v.i += 1;
    s = re.sub(c1, "", line);
    if (not len(s) or (not c1.match(line))):
        return (end_of_comment(n, line));
    return (0);
        
e1 = re.compile("\A\*/\Z");					# end of commentaire bien placé du début de la ligne avec un retour à la ligne juste ensuite.
def end_of_comment(n, line):
    v.fn_entry = 0;
    if (e1.search(line) and v.i > 2):
        v.i = 0;
        return (0);
    return (1);

class StaticVar:
    i = 0;
    fn = [open_comment,current_comment,end_of_comment];
    fn_entry = 0;

v = StaticVar();
def check_comment(n, line):
    if (v.fn[v.fn_entry](n, line)):
        print("L%i -> Commentaire malformé." %(n) + "\n" + line);
        return (1);
    return (0);
