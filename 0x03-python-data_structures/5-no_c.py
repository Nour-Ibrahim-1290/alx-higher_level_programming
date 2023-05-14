#!/usr/bin/python3

def no_c(my_string):
    return ''.join([e for e in list(my_string) if e != 'c' and e != 'C'])
