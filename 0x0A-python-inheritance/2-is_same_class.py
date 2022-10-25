#!/usr/bin/python3
"""
function that returns true if object is exactly
an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    function definition with parameters
    obj and a_class
    """

    if type(obj) == a_class:
        return True
    else:
        return False
