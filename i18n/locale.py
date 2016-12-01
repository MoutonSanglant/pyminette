# coding: utf8

from i18n.fr import *
from i18n.nm import *

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

class Locale:
    value = {};
    color = VisibleColor();

def setLang(lang):
    if (lang == "fr"):
        locale.value = msg_fr;
    else:
        locale.value = msg_nm;

def fail(msg):
    return (locale.color.FAIL + msg + locale.color.EOC);
def warn(msg):
    return (locale.color.WARNING + msg + locale.color.EOC);
def valid(msg):
    return (locale.color.OKGREEN + msg + locale.color.EOC);

def disableColor():
    locale.color = NoneColor();

class Msg:
    def ok_file(self):
        return (valid(locale.value["ok_file"]));
    def err_file(self):
        return (warn(locale.value["err_file"]));
    def bad_comment(self):
        return (fail(locale.value["bad_comment"]));
    def line_too_long(self):
        return (fail(locale.value["line_too_long"]));

msg = Msg();
locale = Locale();