#!/usr/bin/python3
"""Function to check Class Type"""


def is_same_class(obj, a_class):
    """Check if obj is an instance of a_class or not"""

    return True if type(obj) == a_class else False
