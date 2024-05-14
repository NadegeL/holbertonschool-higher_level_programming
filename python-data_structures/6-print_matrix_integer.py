#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    else:
        for row in matrix:
            print(" ".join("{:d}".format(i) for i in row))

        