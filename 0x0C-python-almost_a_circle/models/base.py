#!/usr/bin/python3
"""First class Base"""
import json


class Base():
    """First class known as Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


@staticmethod
def to_json_string(list_dictionaries=[]):
    """Json strings"""
    if list_dictionaries is None or list_dictionaries == []:
        return "[]"
    return json.dumps(list_dictionaries)
