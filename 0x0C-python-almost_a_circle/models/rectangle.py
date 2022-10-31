#!/usr/bin/python3
"""
Class rectangle
"""


from models.base import Base


class Rectangle(Base):
    """
    define class Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super(Rectangle, self).__init__(id)

    # getters
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    # setters
    @width.setter
    def width(self, value):
        self.integer_validator("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        self.integer_validator("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        self.integer_validator("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        self.integer_validator("y", value)
        self.__y = value

    @staticmethod
    def integer_validator(name, value):
        """
        function to validates an integer
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if name == "x" or name == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

        elif value <= 0:
            raise ValueError("{} must be > than 0".format(name))

    def area(self):
        """method that return the area of
        rectangle
        """

        return self.__height * self.__width

    def display(self):
        """method that prints the rectangle
        to stdout
        """

        rectangle = ""
        print("\n" * self.y, end="")
        for i in range(self.height):
            rectangle += (" " * self.x) + ("#" * self.width) + "\n"
        print(rectangle, end="")

    def __str__(self):
        """override the str method
        """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """ update to use **kwargs
        """

        if args is not None:
            for k, v in kwargs.items():
                self.__setattr__(k, v)
        return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass
