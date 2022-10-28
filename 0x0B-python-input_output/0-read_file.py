#!/usr/bin/python3
"""
function to read text
"""


def read_file(filename=""):
    """
    read from filename
    """

    with open("", "r", encoding="utf-8") as f:
        print(f.read())