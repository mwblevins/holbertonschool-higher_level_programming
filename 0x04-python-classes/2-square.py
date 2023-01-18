#!/usr/bin/python3

"""Class Documentation"""


class Square:
    """Class square with private size"""
    pass


def __init__(self, size=0):
    """init method of class Square
    """
    if (not isinstance(_size, int)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size
"""Return area of a square"""


def area(self) -> int:
    return self.__size ** 2
