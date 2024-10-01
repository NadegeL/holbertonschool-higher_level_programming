#!/usr/bin/python3
"""Write a script that adds all arguments to a Python list,
and then save them to a file"""

import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def add_item():
    """import add_item"""
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    for arg in sys.argv[1:]:
        items.append(arg)
    save_to_json_file(items, "add_item.json")
    
if __name__ == "__main__":
    add_item()
