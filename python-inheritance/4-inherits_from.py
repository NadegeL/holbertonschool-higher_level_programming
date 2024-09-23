#!/usr/bin/python3
""" function that returns the object inherited from a class"""


def inherits_from(obj, a_class):
    """ function that returns the object inherited from a class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
