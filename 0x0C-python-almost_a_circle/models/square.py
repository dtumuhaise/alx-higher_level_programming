#!/usr/bin/python3
"""
Square class inheriting from the rectangle
class
"""


from re import X
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    define Square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        kwargs and args
        """

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

        for key, value in kwargs.items():
            if args is not None and args is not []:
                break
            else:
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

        def to_dictionary(self):
            """ returns dict representation of rectangle
            """

            return dict((key, value) for (key, value)
                        in self.__dict__.items())
