#!/usr/bin/python3


def no_c(my_string):
    new = my_string
    print(my_string.translate({ord('c'): None}), {ord('C'): None})
    return new
