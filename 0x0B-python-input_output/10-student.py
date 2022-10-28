#!/usr/bin/python3
"""module to  define a class
"""


class Student:
    """define methods for the student class
    """

    def __init__(self, first_name, last_name, age):
        """__init__ method
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        method that retrieves a dict rep of student
        """

        if isinstance(attrs, str):
            return self.attrs
        else:
            return self.__dict__
