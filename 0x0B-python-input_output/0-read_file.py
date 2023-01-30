#!/usr/bin/python3
"""Task 0"""


def read_file(filename=""):
    """Open new file and print the lines"""
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end="")
