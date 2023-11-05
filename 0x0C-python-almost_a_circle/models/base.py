#!/usr/bin/python3

"""This module holds the Bae Class of Almost A Circle Project."""


class Base():
    """Base Class of Python Almost A Circle

        ATRIBUTES:
        ----------
        __nb_objects (int): count of Base instances
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initiating a new instance of Class Base

            ARGUMENTS:
            ----------
            id (int): id of new Base Object
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
