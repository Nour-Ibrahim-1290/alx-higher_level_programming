#!/usr/bin/python3

"""Define a Square Class"""


class Square:
    """Represent a Square"""

    def __init__(self, size=0):
        """
        Args:
            self: used by Python to initiate Square instances
            size (int): size of Square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Return: area of Square instance using its size
        """
        return self.__size * self.__size
