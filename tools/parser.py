# coding: utf8

from i18n.locale import msg;

def test_line_length(l_number, line):
    c = 0;
    for char in line:
        if (char == '\t'):
            c += (4 - c%4);
        else:
            c += 1;
    if (c > 80):
        print (msg.line_too_long() %(l_number, c));
        print(line);
        return (1);
    return (0);
