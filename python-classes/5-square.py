#!/usr/bin/python3

class Square:
    """ this is class Square"""
    def __init__(self, size=0):
        """size in private instance attribute"""
        while not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._size = size

    @property
    def size(self):
        """public instance return size"""
        return self._size

    @size.setter
    def size(self, value):
        """public instance return size"""
        while not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """public instance return current square area"""
        return self._size ** 2

    def my_print(self):
        """print square with #"""
        for i in range(self._size):
            print("#" * self._size)
        if self._size == 0:
            print()
