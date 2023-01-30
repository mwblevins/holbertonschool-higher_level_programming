#!/usr/bin/python3
"""Task 6"""
import json


def load_from_json_file(filename):
    """From python"""
    with open(filename, 'r') as f:
        contents = f.read()
        obj = json.loads(contents)
        return obj
