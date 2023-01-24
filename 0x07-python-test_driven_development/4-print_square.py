#!/usr/bin/python3
"""4-print_square"""


def print_square(size):
    """prints a square with #"""
    if not isinstance(size, (int)):
        if isinstance(size, float) and size > 0:
            size = int(size)
        else:
            raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("{}".format('#' * size))
