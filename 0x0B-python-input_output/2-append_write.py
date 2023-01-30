#!/usr/bin/python3
"""Task 2"""


def append_write(filename="", text=""):
    """appends"""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
