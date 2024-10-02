#!/usr/bin/python3
"""Create a basic serialization module"""

import json


def serialize_and_save_to_file(data, filename):
    """serialize and save data to a file"""
    with open(filename, 'w') as file:
        file.write(json.dumps(data))
        
def load_and_deserialize(filename):
    """deserialize and load data from a file"""
    with open(filename, 'r') as file:
        return json.loads(file.read())
