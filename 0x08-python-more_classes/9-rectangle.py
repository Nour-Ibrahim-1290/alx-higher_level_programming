#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Define a new Object instance of Rectangle
        Args:
            width (int): The width of the new rectangle object.
            height (int): The height of the new rectangle object.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

        pl = [str(self.print_symbol) * self.width for i in range(self.height)]
        return '\n'.join(pl)

    def __repr__(self):
        """Represent the object as a printable string."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Message in case of deleting an instance."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area.

        Raises:
            TypeError:
            If either rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Create a new instance where height=width=size"""
        return cls(size, size)
