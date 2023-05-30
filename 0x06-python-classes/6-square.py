#!/usr/bin/python3

"""Define a Square Class"""


class Square:
    """Represent a Square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size (int): size of Square
            position (Tuple): where is the square (x, y)
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current size of the square."""
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

    @property
    def position(self):
        """Get the current size of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of Square instance (x, y)"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Return: area of Square instance using its size
        """
        return self.__size * self.__size

    def my_print(self):
        """Print square in # chars"""
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for k in range(self.position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
