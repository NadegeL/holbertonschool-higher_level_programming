#!/usr/bin/python3
"""write a class square that inherits from rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square that inherits from rectangle"""

    def __init__(self, size):
        """method to initialize square
        and use super() function
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Public instance method"""
        return self.__size ** 2
