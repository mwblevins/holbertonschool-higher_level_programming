#!/usr/bin/python3
"""A square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Makes a square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.validate("width", value)
        self.width = value
        self.height = value

    def __str__(self):
        """Returns str representation of Square"""
        return '[Square] ({}) {}/{} - {}'.format(
            self.id,
            self.x,
            self.y,
            self.width
        )
