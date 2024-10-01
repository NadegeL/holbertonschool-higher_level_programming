#!/usr/bin/python3
"""Write a function that returns the dictionary
description withsimple data structure 
(list, dictionary, string, integer and boolean)
for JSON serialization of an object:"""


def class_to_json(obj):
    """verify instance obj"""
    if isinstance(obj, dict):
        return {k: obj.__dict__[k] for k in obj.__dict__ if k in obj.__dict__}
    elif isinstance(obj, list):
        return [class_to_json(i) for i in obj]
    elif isinstance(obj[str, bool, int]):
        return obj
    else:
        return obj.__dict__
