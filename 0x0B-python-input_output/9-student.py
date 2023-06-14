#!/usr/bin/python3
"""Class Student that defines a Student entity"""


class Student:
    """Module represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize Module"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method to_json"""
        return self.__dict__
