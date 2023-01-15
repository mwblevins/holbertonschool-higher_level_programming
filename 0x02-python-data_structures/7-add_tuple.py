#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    ay = [0, 0]
    be = [0, 0]
    for i in range(0, 2):
        if (len(tuple_a) > i):
            ay[i] = tuple_a[i]
        if (len(tiuple_b) > i):
            be[i] = tuple_b[i]
    return tuple((ay[0] + be[0], ay[1] + be[1]))
