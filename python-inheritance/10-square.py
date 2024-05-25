#!/usr/bin/python3
"""subclass of subclass with super()"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """write a subclass Square"""

    def __init__(self, size):
        """method to initialize square
        and use super() function
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2
