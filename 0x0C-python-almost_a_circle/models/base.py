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


def to_json_string(list_dictionaries=[]):
    """Json strings"""
    list_dictionaries = list_dictionaries or []
    return json.dumps(list_dictionaries)
