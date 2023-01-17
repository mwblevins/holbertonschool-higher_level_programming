#!/usr/bin/python3

"""Class documentation"""


class Square:
    """Defines a class Square
    """
    pass

    def __init__(self, size=0):
        """init method of class Square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
