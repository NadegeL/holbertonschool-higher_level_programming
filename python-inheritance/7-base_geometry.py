#!/usr/bin/python3
"""Write an empty class BaseGeometry."""


class BaseGeometry:
    """it is an empty class"""

    def area(self):
        """instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """public instance method"""

        if not isinstance(name, str):
            raise TypeError(f"{name} must be a string")

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
