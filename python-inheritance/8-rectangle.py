#!/usr/bin/python3
"""write my first inheritance"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initialisation a rectangle 
            with integer_validator
        """
        self.__width = width
        self.integer_validator("width", width)

        self.__height = height
        self.integer_validator("height", height)
