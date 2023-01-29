#!/usr/bin/python3
"""task 10"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ new class, square"""
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
