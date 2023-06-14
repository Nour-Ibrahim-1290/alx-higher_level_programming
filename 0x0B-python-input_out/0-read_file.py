#!/usr/bin/python3
"""Function reads txt file"""


def read_file(filename=""):
    """reads a txt file with (UTF8) encoding
    Prints it content to stdout
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
