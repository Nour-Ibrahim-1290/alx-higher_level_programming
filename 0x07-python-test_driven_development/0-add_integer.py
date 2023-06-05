#!/usr/bin/python3
"""Define an integer summation function

All numbers are casted into integers before summation.

Raises: TypeError: in case that any of the arguments is non-number."""

def add_integer(a, b=98):
    """Return the addition of two numbers a and b.

    Chacks type of argument and raises TypeError in case of non-number arguments."""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
