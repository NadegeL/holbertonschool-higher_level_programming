#!/usr/bin/python3
"""Write a class Square"""


class Square:
    """Write a class Square that defines a square by: (based on 3-square.py)"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """size retrieve"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2
