#!/usr/bin/python3
"""Matrix divided mod"""


def matrix_divided(matrix, div):
    """divide a matrix elements by div"""

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)\
            of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    i = len(matrix[0])
    for row in matrix:
        if len(row) != i:
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if type(x) not isinstance(int, float):
                raise TypeError("matrix must be a matrix (list of lists)\
                    of integers/floats")
    matrix = [[round(x / div, 2) for x in row] for row in matrix]
    return matrix
