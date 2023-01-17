#!/usr/bin/python3

"""This is for the size of the square i believe"""


class Square:
    """Defines a class Square
    """

    def __init__(self, size=0):
        """init method of class Square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._-size = size
