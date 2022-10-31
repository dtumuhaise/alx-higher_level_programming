#!/usr/bin/python3
"""
Square class inheriting from the rectangle
class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    define Square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
