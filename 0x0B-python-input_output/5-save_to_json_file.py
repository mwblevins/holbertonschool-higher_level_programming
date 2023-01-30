#!/usr/bin/python3
"""Task 5"""
import json


def to_json_file(my_obj, filename):
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
