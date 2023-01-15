#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    val_a = [0, 0]
    val_b = [0, 0]
    for i in range(0, 2):
        if (len(tuple_a) > i):
            val_a[i] = tuple_a[i]
        if (len(tuple_b) > i):
            val_b[i] = tuple_b[i]
    return tuple((val_a[0] + val_b[0], val_a[1] + val_b[1]))
