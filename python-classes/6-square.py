#!/usr/bin/python3
"""Write a class Square"""


class Square:
    """ this is class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """instance attribut size and position"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """private instance return size"""
        return self.__size

    @size.setter
    def size(self, value):
        """private instance return size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """private instance return position"""
        return self.__position

    @position.setter
    def position(self, value):
        """private instance must be a tuple of 2 positive integers"""
        for i in tuple(value):
            if not isinstance(i, int):
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
            if i < 0:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
            if len(value) != 2:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """public instance return current square area"""
        return self.__size ** 2

    def my_print(self):
        """print square with #"""
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
