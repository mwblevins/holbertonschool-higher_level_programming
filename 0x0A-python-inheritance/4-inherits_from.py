#!/usr/bin/python3
"""Task 4"""


def inherits_from(obj, a_class):
    """Inheritance"""
    return(issubclass(type(obj), a_class) and type(obj) is not a_class)
