#!/usr/bin/python3
"""
module to define a function
"""


import json


def save_to_json_file(my_obj, filename):
    """
    define function that writes object to text file
    """

    with open(filename, "w", encoding="utf8") as f:
        return json.dump(my_obj, f)
