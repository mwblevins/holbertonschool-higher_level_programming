#!/usr/bin/python3
"""Class for a simple rectangle"""


class Rectangle:
    """Class for a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        area = self.height * self.width
        return area

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        perimeter = 2 * (self.width + self.height)
        return perimeter

    def __str__(self):
        mystr = ""
        if (self.width == 0 or self.height == 0):
            return (mystr)
        mystr = (('#' * self.width)+'\n')*(self.height-1) + ('#' * self.width)
        return mystr

    def __repr__(self):
        return ("Rectangle({0}, {1})".format(self.width, self.height))
