#!/usr/bin/python3
"""
module to define function that
prints my name

"""


def say_my_name(first_name, last_name=""):
    """Prints firs and last name

    Args:
    First_name: first name string.
    last_name: last name string defaults to empty string

    Raises:
    TypeError: if args are not strings

    """

    if type(first_name) in (int, float):
        raise TypeError("first_name must be a string")
    elif type(last_name) in (int, float):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
