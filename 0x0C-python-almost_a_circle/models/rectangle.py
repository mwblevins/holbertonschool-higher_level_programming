#!/usr/bin/python3
"""Rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """creates class rectangle with protected attributes"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self. y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of a rectangle"""
        return self.width * self.height

    def display(self):
        """Prints the rectangle"""
        row = ' ' * self.x + '#' * self.width
        for i in range(self.height):
            print(row)
        for i in range(self.y):
            print()

    def __str__(self):
        """Override"""
        strrect = "[Rectangle] " + "({}) ".format(self.id)
        strrect += "{}/{} - ".format(self.x, self.y)
        strrect += "{}/{}".format(self.width, self.height)
        return strrect

    def update(self, *args, **kwargs):
        """Updates"""
        if (args is None or args == ()) and kwargs is not None:
            args = [kwargs.get("id"), kwargs.get("width"),
                    kwargs.get("height"), kwargs.get("x"),
                    kwargs.get("y")]
        try:
            self.id = args[0] or self.id
            self.width = args[1] or self.width
            self.height = args[2] or self.height
            self.x = args[3] or self.x
            self.y = args[4] or self.y
        except IndexError:
            return

    def to_dictionary(self):
        """Turn this rect into a dict"""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
