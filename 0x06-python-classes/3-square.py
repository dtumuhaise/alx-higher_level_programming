#!/usr/bin/python3
"""Class Square"""


class Square:
    """init size"""
    def __init__(self, __size=0):
        self.__size = __size
        if not type(__size) is int:
            raise TypeError("size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """returns area of square"""
        return self.__size ** 2


area1 = Square()
area1.area()
