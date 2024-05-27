#!/usr/bin/python3
"""Write a function that writes a string to a text file
(UTF8) and returns the number of characters written:
"""


def write_file(filename="", text=""):
    """function that writes a string"""

    with open(filename, 'w', encoding="UTF-8") as f:
        nb_of_char = f.write(text)
        return len(text)
