#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    newlist = []
    for i in my_list:
        newlist.append(i % 2 == 0)
    return newlist
