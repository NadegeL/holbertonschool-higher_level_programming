#!/usr/bin/python3
"""Write a class Square"""


class Square:
    """Write a class Square that defines a square by: (based on 1-square.py)"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be an integer")
        self.__size = size
