#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    newdict = dict({x: 2*y for x, y in a_dictionary.items()})
    return newdict
