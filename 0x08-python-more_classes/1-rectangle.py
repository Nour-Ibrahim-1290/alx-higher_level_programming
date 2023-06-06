#!/usr/bin/python3
"""
Defines a Rectangle class.
"""


class Rectangle:
    """
    Represents a rectangle.
    """

    __width = 0
    __height = 0

    def __init__(self, width=0, height=0):
        """
        Define a new Object instance of Rectangle
        Args:
            width (int): The width of the new rectangle object.
            height (int): The height of the new rectangle object.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieve width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set weight as value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieve width
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set weight as value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__height = value
