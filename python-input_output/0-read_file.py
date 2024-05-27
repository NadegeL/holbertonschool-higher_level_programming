#!/usr/bin/python3
"""Write a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """protype of function"""
    with open(filename, "r", encoding="UTF-8") as f:
        my_file = f.read()
        print("f", end="")