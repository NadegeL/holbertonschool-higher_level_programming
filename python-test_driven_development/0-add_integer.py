#!/usr/bin/python3
"""
    This module provides a function `add_integer` to add two integers.
"""


def add_integer(a, b=98):
    """
    a and b must be integers or floats,
    a and b must be first casted to integers if they are float
    Returns an integer: the addition of a and b
    You are not allowed to import any module
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
