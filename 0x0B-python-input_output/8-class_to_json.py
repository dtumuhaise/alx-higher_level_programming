#!/usr/bin/pyton3
"""
module to define function
"""


import json


def class_to_json(obj):
    """
    function returns dict with simple data structure for
    JSON serialization of an object
    """

    return json.dumps(obj.__dict__)
