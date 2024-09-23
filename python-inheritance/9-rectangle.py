#!/usr/bin/python3
"""Write a class Rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initialisation a rectangle
            with integer_validator
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Public instance method:"""
        return self.__width * self.__height

    def __str__(self):
        """should return a string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def __repr__(self):
        """method appel str et print la chaine"""
        return (self.__str__)
