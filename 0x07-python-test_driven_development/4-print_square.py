#!/usr/bin/python3
"""
define module to print squars
with character #
"""


def print_square(size):
    """Module to print a square with character


    Args:
        size: size length of the square

    Raises:
        TypeError: when size is not an integer
        ValueError: when size is less than 0
        TypeError: if size is float and < 0
    """

    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) != int:
        raise TypeError("size must be an integer")

    for i in range(size):
        for i in range(size):
            print('#', end='')
        print()
