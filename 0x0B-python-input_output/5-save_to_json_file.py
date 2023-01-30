#!/usr/bin/python3
"""Task 5"""
import json


def save_to_json_file(my_obj, filename):
    """Forgetting everything tbh"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
