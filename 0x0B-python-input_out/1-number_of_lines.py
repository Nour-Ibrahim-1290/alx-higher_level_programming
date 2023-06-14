#!/usr/bin/python3
"""Function that returns the number of lines txt file"""


def number_of_lines(filename=""):
    """Function to count the number of lines"""
    if filename == "" or type(filename) != str:
        return 0
    counter = 0
    with open(filename, 'r') as f:
        for line in f:
            counter += 1
    return counter
