#!/usr/bin/python3
"""list attributes"""


def lookup(obj):
    """List Attributes"""
    start = list(obj.__dict__.keys())
    start.extend(i for i in dir(obj) if i not in start)
    start.sort()
    return start
