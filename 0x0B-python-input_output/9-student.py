#!/usr/bin/python3
"""Task 9"""


class Student:
    """again with the docs"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return (vars(self))
