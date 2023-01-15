#!/usr/bin/python3


def no_c(my_string):
    _list = [char for char in my_string if char != 'c']
    _list = [char for char in _list if char != 'C']
    my_string = "".join(_list)
    return my_string
