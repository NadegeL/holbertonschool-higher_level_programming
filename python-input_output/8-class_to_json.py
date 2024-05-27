#!/usr/bin/python3
"""Write a function that returns the dictionary description"""


def class_to_json(obj):
    """
    Returns the dictionary
    obj: The object to convert to a dictionary.
    """
    return obj.__dict__
