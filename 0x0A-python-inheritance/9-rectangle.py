#!/usr/bin/python3
"""Project 0x07 Task 2"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class Bro"""
    def __init__(self, width, height) -> None:
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self) -> str:
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
