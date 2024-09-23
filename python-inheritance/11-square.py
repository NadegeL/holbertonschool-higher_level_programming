#!/usr/bin/python3
"""write a class square that inherits from rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square that inherits from rectangle"""

    def __init__(self, size):
        """method to initialize square
        and use super() function
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Public instance method"""
        self.area = self.__size ** 2
        return self.area

    def __str__(self):
        """should return a string"""
        return "[Square] {}/{}".format(self.__size, self.__size)

    def repr(self):
        """method appel str et print la chaine"""
        return (self.__str__)
