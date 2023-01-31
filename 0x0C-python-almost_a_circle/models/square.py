#!/usr/bin/python3
"""A square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Makes a square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns str representation of Square"""
        return '[Square] ({}) {}/{} - {}'.format(
            self.id,
            self.x,
            self.y,
            self.width
        )
