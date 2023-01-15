#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for inner in list(matrix):
        for i, ints, in enumerate(list(inner)):
            if(i != 0):
                print("{}".format(" "), end="")
            print("{:d}".format(ints), end="")
        print()
