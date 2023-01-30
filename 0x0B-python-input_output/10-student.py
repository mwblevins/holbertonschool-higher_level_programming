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
        for key, value in vars(self).items():
            if key in ats:
                ats[key] = value
        return (ats)
