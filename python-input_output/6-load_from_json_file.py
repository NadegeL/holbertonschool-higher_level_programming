#!/usr/bin/python3
"""
Write a function that creates an Object from a “JSON file”
"""

import json


def load_from_json_file(filename):
    """create an obj from a Json file"""
    with open(filename, 'r') as f:
        json_string = f.read()
        return json.loads(json_string)


def write_to_a_new_file(data, new_filename):
    with open(new_filename, 'w') as f:
        json.dump(data, f)
