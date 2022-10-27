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
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))


class Square(Rectangle):
    """
    define class Square inheriting fom rectangle class
    """

    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return ("[Square] " + str(self.__size) + "/" + str(self.__size))
