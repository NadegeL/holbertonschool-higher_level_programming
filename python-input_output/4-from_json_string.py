#!/usr/bin/python3
"""Write a function that returns the JSON
representation of an object (string)
"""

import json


def from_json_string(my_str):
    """method json"""
    return json.loads(my_str)
