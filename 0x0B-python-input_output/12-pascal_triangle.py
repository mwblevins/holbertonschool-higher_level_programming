#!/usr/bin/python3
"""Technical Triangle"""


def pascal_triangle(n):
    """Lets make a triangle"""
    if n <= 0:
        return []
    x = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(x[i-1][j-1] + x[i-1][j])
        row.append(1)
        x.append(row)
    return x
