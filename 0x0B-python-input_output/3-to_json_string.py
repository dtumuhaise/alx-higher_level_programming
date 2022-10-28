#!/usr/bin/python3
import json
"""
module to define a function
"""


def to_json_string(my_obj):
    """
    define function that returns JSON represnentation
    of an object
    """

    return json.dumps(my_obj)
