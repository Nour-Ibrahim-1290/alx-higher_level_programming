#!/usr/bin/python3
"""Class that inherits lists"""


class MyList(list):
    """one function
    """

    def print_sorted(self):
        """print a list of sorted ints"""
        print(sorted(self))
