#!/usr/bin/python3
"""
Write a function that appends a string at the end of a text file
UTF8) and returns the number of characters added:
"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding="UTF-8") as f:
        nb_characters = f.write(text)
        return nb_characters
