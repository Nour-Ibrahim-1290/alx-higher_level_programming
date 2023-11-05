#!/usr/bin/python3

"""This module is to define a child of Base class."""

from models.base import Base


class Rectangle(Base):
    """A Child class of Base to define a rectangle instance.

        ATTRIBUTES:
        -----------
        __width (int): width of a rectangle object.
        __height (int): height of a rectangle object.
        __x (int): starting position on x coordinate.
        __y (int): starting position on y coordinate.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initiate a new Instance of Rectangle class.

            ARGUMENTS:
            ----------
            width (int): public instance attribute.
            height (int): public instance attribute.
            x (int): public instance attribute.
            y (int): public instance attribute.
            id (int): id of Reactangle instance (setten on Base class).

            RAISES:
            -------
            TypeError: If either width, height, x or y is not an integer.
            ValueError: If either width or height <= 0.
            ValueError: IF either x or y < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Set/get width of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set/get width of a Rectangle instance."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/get height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set/get height of a Rectangle instance."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/get x position of a Rectangle instance."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set/get x position of a Rectangle instance."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get y position of a Rectangle instance."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set/get y position of a Rectangle instance."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return Area of a Rectangle instance."""
        return self.__width * self.__height
