#!/usr/bin/python3
""" this is class Square that defines size"""


class Square:
    def __init__(self, size=0):
        """size in private instance attribute"""
        while not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._size = size
