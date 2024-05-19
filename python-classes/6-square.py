#!/usr/bin/python3
"""Write a class Square"""


class Square:
    """Write a class Square that defines a square by: (based on 4-square.py)"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ position retrieve"""
        return self.__position

    @position.setter
    def position(self, value):
        """set position of the square"""
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """print a square with character#"""
        if self.size == 0:
            print("")
            return
        for i in range(self.position[1]):
            print("")
        for i in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
