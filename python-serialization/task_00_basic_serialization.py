#!/usr/bin/env python3
"""
Create a basic serialization module
deserialize the JSON file to recreate the Python Dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """serialize with dump"""
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """deserialize with load"""
    with open(filename, 'r') as f:
        return json.load(f)
