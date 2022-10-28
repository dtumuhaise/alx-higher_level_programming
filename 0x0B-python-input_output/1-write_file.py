#!/usr/bin/python3
"""
module to create a write function
"""


def write_file(filename="", text=""):
    """
    define function to write a string to
    textfile
    """

    with open(filename, "w", encoding="utf8") as f:
        w = f.write(text)
