#!/usr/bin/python3
"""task 10"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self) -> str:
        return "[Square] {}/{}".format(self.__size, self.__size)
