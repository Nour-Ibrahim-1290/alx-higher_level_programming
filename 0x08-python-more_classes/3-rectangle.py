#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle."""

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
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__height = value

    def area(self):
        """Calculate the area of the rectangle instance"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle instance"""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Represent the object as a string."""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return '\n'.join('#' * self.width for i in range(self.height))
