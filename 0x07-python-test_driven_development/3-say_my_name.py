#!/usr/bin/python3
"""A Module with one function to type full name"""


def say_my_name(first_name, last_name=""):
    """Print: Full Name
    Raise: TypeError in case any of the argumrnts is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
