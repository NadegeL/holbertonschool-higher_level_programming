#!/usr/bin/python3
"""verify obj is exactly instance"""


def is_same_class(obj, a_class):
    """
        Write a function that returns True
        otherwise False.
    """
    return type(obj) is a_class


is_same_class(1, int)
is_same_class(1, object)
