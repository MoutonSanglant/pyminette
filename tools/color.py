# coding: utf8

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

def disableColor():
    color.colorSet = NoneColor();