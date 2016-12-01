# coding: utf8

"""
comment_lines = 0;
def test_comment(l_number, line):
    global comment_lines;
    if (line == "/*"):							# TODO replace by regex.
        if (comment_lines != 0):
            print (color.FAIL + "L%i -> Le symbole de nouveau commentaire ne peut etre utilisé ici (recently used)." %(l_number) + color.EOC + "\n" + line);
            return (1);
        comment_lines += 1;
    elif (line == "*/"):						# TODO replace by regex.
        comment_lines += 1;
        if (comment_lines == 0):
            print (color.FAIL + "L%i -> Une ligne de fermeture de commentaire n'a rien à faire ici !" %(l_number) + color.EOC + "\n" + line);
            return (1);
        elif (comment_lines < 3):
            print (color.FAIL + "L%i -> Un commentaire est bien trop court ! line = %i" %(l_number, comment_lines) + color.EOC + "\n" + line);
            comment_lines = 0;
            return (1);
        comment_lines = 0;
    elif (line begin by **):					# TODO replace by regex.
        comment_lines += 1;
        if (size=after regex **(space) or **(tab) has value):	# TODO replace by regex.
            print (color.FAIL + "L%i -> Une ligne de commentaire ne peut etre vide !" %(l_number) + color.EOC + "\n" + line);
            return (1);
    elif (test regex commencant par */ ou /* mais continuant sur la ligne) # TODO regex

    else (comment_line != 0):
        print (color.FAIL + "L%i -> Il devrait y avoir un commentaire ici !" %(l_number) + color.EOC + "\n" + line);
        return (1);
    return (0);
"""