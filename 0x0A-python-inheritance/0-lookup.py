#!/usr/bin/python3
"""Function return list of objects"""


def lookup(obj):
    """return a list of all possible
    fucntions and objects inside a list
    """
    return dir(obj)
