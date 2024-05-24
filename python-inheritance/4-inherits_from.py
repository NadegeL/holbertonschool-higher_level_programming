#!/usr/bin/python3
""" 
function that returns if the object 
is an instance of a class that inherited
"""


def inherits_from(obj, a_class):
    """returns True or False"""
    
    if isinstance(obj, a_class):
        return True
    else:
        return issubclass(obj.__class__, a_class)
