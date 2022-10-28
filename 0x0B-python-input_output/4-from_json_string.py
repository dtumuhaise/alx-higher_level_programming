#!/usr/bin/python3
"""
module to define function
"""


import json


def from_json_string(my_str):
    """
    function retruns an object represented
    by a JSON string
    """

    return json.loads(my_str)
