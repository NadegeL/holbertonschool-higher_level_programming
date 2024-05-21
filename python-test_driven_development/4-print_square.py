#!/usr/bin/python3
"""
print a square
"""


def print_square(size):
    """
    function that print a square
    verify if size is an integer
    if size of lenght is less tha 0
    """
    
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
