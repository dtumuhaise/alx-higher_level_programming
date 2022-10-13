#!/usr/bin/python3
"""class square"""


class Square:
    """a square"""
    def __init__(self, __size=0):
        self.__size = __size
        if not type(__size) is int:
            raise TypeError("size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")
