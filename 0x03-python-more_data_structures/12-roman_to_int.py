#!/usr/bin/python3


def roman_to_int(string_in):
    convert = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    runningSum = 0
    last = None
    if string_in is None or not isinstance(string_in, str):
        return 0
    for x in reversed(list(string_in.upper())):
        i = convert.get(x, 0)
        if last is None or i >= last:
            runningSum += i
        else:
            runningSum -= i
        last = i
    return runningSum
