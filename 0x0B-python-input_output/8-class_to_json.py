#!/usr/bin/python3
"""
module to define function
"""


def class_to_json(obj):
    """
    function returns dict with simple data structure for
    JSON serialization of an object
    """

    return obj.__dict__
