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

        if (type(attrs) == list and
                all(type(i) == str for i in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        method that replaces all attributes of Student
        insatance
        """

        for k, v in json.items():
            setattr(self, k, v)
