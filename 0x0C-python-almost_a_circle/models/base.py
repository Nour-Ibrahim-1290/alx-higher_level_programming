"""This module holds the Bae Class of Almost A Circle Project."""


class Base():
    """Base Class of Python Almost A Circle

        ATRIBUTES:
        ----------
        __nb_objects: private int
        id: public int
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initiating a new instance of Class Base"""
        if id == None:
            self.id = __nb_objects
        else:
            __nb_objects += 1
            self.id = id
