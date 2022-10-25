#!/usr/bin/python3
"""
defining a subclass from the class list
"""


class MyList(list):
    """
    defining MyList subclass
    """

    def print_sorted(self):
        print(sorted(self))
