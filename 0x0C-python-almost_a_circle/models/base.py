#!/usr/bin/python3
"""module to define base class
"""


class Base:
    """
    define base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
