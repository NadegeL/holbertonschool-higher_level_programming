#!/usr/bin/python3
"""Write an empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """ Class Rectangle"""

    def __init__(self, width=0, height=0):
        """Method that initializes the instance"""
        self.__width = width
        self.__height = height

        @property
        def width(self):
            """Method that returns the value of the width"""
            return self.__width

        @width.setter
        def width(self, value):
            """Method that returns the value of the width"""
            while i in value:
                if not isinstance(i, int):
                    raise TypeError("width must be an integer")
                if i < 0:
                    raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """Method that returns the value of the height"""
            return self.__height

        @height.setter
        def height(self, value):
            """Method that returns the value of the height"""
            while i in value:
                if not isinstance(i, int):
                    raise TypeError("height must be an integer")
                if i < 0:
                    raise ValueError("height must be >= 0")
            self.__height = value
