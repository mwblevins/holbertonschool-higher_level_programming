#!/usr/bin/python3
"""First class Base"""
import json


class Base:
    """First class known as Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


@staticmethod
def to_json_string(list_dictionaries):
    if list_dictionaries is None or list_dictionaries == []:
        return "[]"
    return json.dumps(list_dictionaries)


@classmethod
def save_to_file(cls, list_objs):
    with open((cls.__name__ + ".json"), 'w') as jasonfile:
        if list_objs is None:
            jasonfile.write("[]")
        else:
            richards = [ii.to_dictionary() for ii in list_objs]
            jasonfile.write(Base.to_json_string(richards))


@staticmethod
def from_json_string(json_string):
    if json_string == "[]" or json_string is None:
        return []
    else:
        return json.loads(json_string)


@classmethod
def create(cls, **dictionary):
    if dictionary:
        if cls.__name__ == "Square":
            nrich = cls(1)
        elif cls.__name__ == "Rectangle":
            nrich = cls(1, 1)
        nrich.update(**dictionary)
        return nrich


@classmethod
def load_from_file(cls):
    fname = cls.__name__ + ".json"
    try:
        with open(fname) as jason:
            jay = Base.from_json_string(jason.read())
            return [cls.create(**x) for x in jay]
    except IOError:
        return []
