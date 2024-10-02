#!/usr/bin/python3
"""Write a function that returns the dictionary
description withsimple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object:"""


def class_to_json(obj):
    """verify instance obj"""
    return obj.__dict__
