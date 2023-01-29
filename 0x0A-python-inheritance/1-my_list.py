#!/usr/bin/python3
"""Inheritance"""


class Mylist(list):
    """inheritance"""
    def print_sorted(self):
        _i = self[:]
        _i.sort()
        print(_i)
