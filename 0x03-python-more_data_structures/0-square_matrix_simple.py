#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = ""
    for x in matrix:
        new_matrix.append([i**2 for i in x])
    return new_matrix
