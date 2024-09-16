#!/usr/bin/python3
"""Write a class Square"""


class Square:
    """ this is class Square that defines size"""
    def __init__(self, size=0):
        """size in private instance attribute"""
        while not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """public instance return current square area"""
        return self.__size ** 2
