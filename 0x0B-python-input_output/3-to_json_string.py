#!/usr/bin/python3
"""
module to define a function
"""


import json

def to_json_string(my_obj):
    """
    define function that returns JSON represnentation
    of an object
    """

    return json.dumps(my_obj)
