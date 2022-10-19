#!/usr/bin/python3
"""Module to define Rectangle class"""


class Rectangle:
    """Defines Rectangle with private instance
    width and hieght
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    # setters
    def set_width(self, value):
        if type(value) not in int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.value = value

    def set_height(self, value):
        if type(value) not in int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.value = value

    # getters
    def get_height(self):
        return self.height

    def get_width(self):
        return self.width
