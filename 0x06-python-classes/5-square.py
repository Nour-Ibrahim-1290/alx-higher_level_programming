#!/usr/bin/python3

"""Define a Square Class"""


class Square:
    """Represent a Square"""

    def __init__(self, size=0):
        """
        Args:
            size (int): size of Square
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, size):
        """
        Sets the size of the Square instance
        Args:
            size (int): size of Square instance
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

    def my_print(self):
        """Print square in # chars"""
        if self.__size == 0:
            print()

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
