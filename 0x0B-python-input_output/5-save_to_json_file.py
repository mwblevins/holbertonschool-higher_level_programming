#!/usr/bin/python2
"""Task 5"""
import json


def to_json_file(obj, filename):
    with open(filename, 'w') as f:
        json.dump(obj, f)
