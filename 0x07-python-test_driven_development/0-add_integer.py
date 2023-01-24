#!/usr/bin/python3
"""add_integer module"""


def add_integer(a, b=98):
    """Adds two ints"""
    
    a = (round(a) if isinstance(a, (float, int)) else None)
    b = (round(b) if isinstance(b, (float, int)) else None)
    if a is None:
        raise TypeError("a must be an integer")
    if b is None:
        raise TypeError("b must be an integer")
    return int(round(a + b))