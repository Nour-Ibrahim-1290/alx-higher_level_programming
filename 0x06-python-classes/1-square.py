#!/usr/bin/python3

"""Define a Square Class"""


class Square:
    """Represent a Square"""

    __size = 0

    def __init__(self, size):
        """
        Args:
            self: used by Python to initiate Square instances
            size (int): size of Square
        """
        self.__size = size
