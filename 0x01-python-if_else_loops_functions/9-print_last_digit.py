#!/usr/bin/python3


def print_last_digit(number):
    mynum = abs(number) % 10
    print("{}".format(mynum), end="")
    return (mynum)
