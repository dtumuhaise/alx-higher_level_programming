#!/usr/bin/python3
"""
module to define a function
"""


import json


def save_to_json_file(my_obj, filename):
    """
    define function that writes object to test file
    """

    with open(filename, "w", encoding="utf8") as my_obj:
        json.dump(my_obj, filename)