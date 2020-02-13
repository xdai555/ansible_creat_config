#!usr/bin/python

import sys,os
#print(os.getcwd())
sys.path.append(os.getcwd())
#print(sys.path)
from files.bracket_expansion import expand

def bracket2list(a):
    return expand(a)

class FilterModule(object):
    def filters(self):
        return {
            'bracket2list': bracket2list
                }
