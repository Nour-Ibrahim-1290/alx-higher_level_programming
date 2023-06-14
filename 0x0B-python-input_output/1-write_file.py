#!/usr/bin/python3
"""Function that writes a string to txt file with (UTF8)"""


def write_file(filename="", text=""):
    """ Write text to file
    Return: number of characters written
    """
    with open(filename, 'w') as f:
        return f.write(text)
