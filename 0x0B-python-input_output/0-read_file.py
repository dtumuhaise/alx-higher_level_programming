#!/usr/bin/python3
"""
function to read text
"""


def read_file(filename=""):
    """
    read from filename
    """

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(f.read())
