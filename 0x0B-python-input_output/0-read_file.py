#!/usr/bin/python3
"""Task 0"""


def read_file(filename=""):
    """Open new file and print the lines"""
    with open(filename, 'r', encoding='utf-8') as file:
        file_contents = file.read()
        print(file_contents)
