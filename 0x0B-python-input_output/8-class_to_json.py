#!/usr/bin/python3
"""Task 8"""


def class_to_json(obj):
    """no import"""
    data = obj.__dict__
    serial = {}
    for key, value in data.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serial[key] = value
    return serial
