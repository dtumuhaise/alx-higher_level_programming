#!/usr/bin/python3
"""
function that returns true if object is an
instance of or is the object is an instance
of a class
"""


def is_kind_of_class(obj, a_class):
    """
    defining the function with
    parameters obj and class
    """

    return issubclass(type(obj), a_class)
    if type(obj) == a_class:
        return True
    else:
        return False
