#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == 0:
        print({""}.format(matrix))
    else:
        for row in matrix:
            print(" ".join(map(str,row)))
        
