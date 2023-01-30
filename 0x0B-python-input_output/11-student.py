#!/usr/bin/python3
"""Task 10"""


class Student:
    """again with the docs"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns description"""

        if attrs is None:
            return (vars(self))
        ats = {}
        for i in attrs:
            try:
                ats[i] = vars(self)[i]
            except:
                Exception
        return (ats)

    def reload_from_json(self, json):
        """Takes info from Json and loads to dict"""
        self.__dict__.update(json)
