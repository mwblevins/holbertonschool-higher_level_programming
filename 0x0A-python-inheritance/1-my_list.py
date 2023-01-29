#!/usr/bin/python3
"""Inheritance"""


class Mylist(list):
    """inheritance task one"""
    def print_sorted(self):
        _t = self[:]
        _t.sort()
        print(_t)
