#!/usr/bin/python3
"""
module defines a class
"""


class BaseGeometry:
    """
    define module area
    """

    def area(self):
        raise Exception("area() is not implemented")

    """
    define methode integer_validator
    """

    def integer_validator(self, name, value):
        """
        function to validates an integer
        """

        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    defining class rectangle modules
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)
