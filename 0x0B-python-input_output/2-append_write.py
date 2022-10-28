#!/usr/bin/python3
"""
module to define a function
"""


def append_write(filename="", text=""):
    """function to addend text
    to file
    """

    with open(filename, "a", encoding="utf8") as f:
        f.write(text)
