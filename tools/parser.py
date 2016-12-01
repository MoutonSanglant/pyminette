
class VisibleColor:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    EOC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class NoneColor:
    HEADER = ''
    OKBLUE = ''
    OKGREEN = ''
    WARNING = ''
    FAIL = ''
    EOC = ''
    BOLD = ''
    UNDERLINE = ''

class Color:
    colorSet = VisibleColor();

color = Color();

def test_line_length(l_number, line):
    c = 0;
    for char in line:
        if (char == '\t'):
            c += (4 - c%4);
        else:
            c += 1;
    if (c > 80):
        print (color.colorSet.FAIL + "L%i -> Cette ligne excède 80 caractères: %i caractères trouvés !" %(l_number, c) + color.colorSet.EOC + "\n" + line);
        return (1);
    return (0);
