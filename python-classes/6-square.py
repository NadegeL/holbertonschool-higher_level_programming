#!/usr/bin/python3
""" this is class Square that defines size"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """instance attribut size and position"""
        while not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._size = size
        self._position = position

    @property
    def size(self):
        """private instance return size"""
        return self._size

    @size.setter
    def size(self, value):
        """private instance return size"""
        while not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """private instance return position"""
        return self.position

    @position.setter
    def position(self, value):
        """private instance must be a tuple of 2 positive integers"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """public instance return current square area"""
        return self._size ** 2

    def my_print(self):
        """print square with #"""
        for _ in range(self._position[1]):
            print()
        for i in range(self._size):
            print(" " * self._position[0] + "#" * self._size)
