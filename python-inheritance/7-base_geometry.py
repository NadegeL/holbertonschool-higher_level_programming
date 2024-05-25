#!/usr/bin/python3
"""Write an empty class BaseGeometry."""


class BaseGeometry:
    """it is an empty class"""

    def area(self):
        """instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """public instance method"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
