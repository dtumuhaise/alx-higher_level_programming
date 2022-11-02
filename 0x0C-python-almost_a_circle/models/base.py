#!/usr/bin/python3
"""module to define base class
"""

import json


class Base:
    """
    define base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representatuon
        """
        if list_dictionaries is None or []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """method writes JSON string representation
        to a file
        """

        filename = cls.__name__ + ".json"
        contents = []

        if list_objs is not None:
            for obj in list_objs:
                obj = obj.to_dictionary()
                json_dict = json.loads(cls.to_json_string(obj))
                contents.append(json_dict)

        with open(filename, "w") as f:
            json.dump(contents, f)

    @staticmethod
    def from_json_string(json_string):
        """ returns list of the JSON string representation
        """

        if json_string is None or []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns instance with attributes already set
        """

        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            mod = Rectangle(2, 7)
        elif cls.__name__ == "Square":
            mod = Square(6)
        mod.update(**dictionary)
        return mod
