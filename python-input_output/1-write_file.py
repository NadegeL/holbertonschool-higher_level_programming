#!/usr/bin/python3
"""function that writes a string to a text file (UTF8)
and returns the number of characters written"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding='UTF-8') as file:
        file.write = text
        return len(text)
