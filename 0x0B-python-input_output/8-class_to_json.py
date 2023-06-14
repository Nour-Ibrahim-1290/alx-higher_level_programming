#!/usr/bin/python3
"""Function that returns dict description with data structure"""


def class_to_json(obj):
    """Transform Object into dict
    Return: builds a dictionary
    """
    return obj.__dict__
