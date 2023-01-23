#!/usr/bin/python3
"""Simple Square Project, not over documented"""


class Square:
    """Class representing a simple square"""
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __init__(self, _size=0):

        self.size = _size

    def area(self):
        return self.__size ** 2
