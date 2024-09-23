#!/usr/bin/python3
"""write an empty class"""


class BaseGeometry:
    """empty class"""
    def area(self):
        """Public instance method:"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method:"""
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
