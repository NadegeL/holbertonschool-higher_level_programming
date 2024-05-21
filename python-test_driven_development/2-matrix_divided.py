#!/usr/bin/python3
"""
Write a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    matrix must be a list of lists of integers or floats, otherwise
    raise a TypeError exception with
    the message matrix must be a matrix (list of lists) of integers/floats
    """

    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError
    ("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(elem, (int, float))
               for row in matrix for elem in row):
        raise TypeError
    ("matrix must be a matrix (list of lists) of integers/floats")

    row_lengths = [len(row) for row in matrix]
    if len(set(row_lengths)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    matrice = [[round(elem / div, 2)
                for elem in row] for row in matrix]

    return matrice
