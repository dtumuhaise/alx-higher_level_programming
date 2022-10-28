#!/usr/bin/python3
"""
module to define a function
"""


import json


def load_from_json_file(filename):
    """
    define function that creates object from
    JSON file
    """

    with open(filename) as f:
        return json.loads(f)
