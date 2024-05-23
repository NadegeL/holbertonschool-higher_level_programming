#!/usr/bin/python3
"""Write an empty class that define a rectangle"""


class Rectangle:
    """an empty rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """width retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        """width value set"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        """value of height set"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """find perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """return a string representation of rectangle"""
        if self.__width == 0 or self.height == 0:
            return ""

        lines = ["#" * self.__width for _ in range(self.height)]
        return "\n".join(lines)

    def __repr__(self):
        """ create a repr de str rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"
