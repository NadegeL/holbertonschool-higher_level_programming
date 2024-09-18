#!/usr/bin/python3
"""Write an empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """ Class Rectangle"""

    def __init__(self, width=0, height=0):
        """Method that initializes the instance"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Method that returns the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method that returns the value of the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Method that returns the value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method that returns the value of the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method that returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Method that return the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Method to print a string representation"""
        if self.__height == 0 or self.__width == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)
    def my_print(self):
        """Method to print with # """
        print(self.__str__())
