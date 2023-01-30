#!/usr/bin/python3
"""Task 1"""


def write_file(filename="", text=""):
    """Forgot"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
    return len(text)
