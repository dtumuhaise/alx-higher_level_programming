#!/usr/bin/python3
"""
Function that returns true if object is
an instance of a class that inherited
from a specified class
"""


def inherits_from(obj, a_class):
    """
    function defination with arguments as
    obj and a_class
    """

    return isinstance(obj, a_class) and type(obj) != a_class
