#!/usr/bin/python3
"""function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    with open(filename, 'r', encoding='UTF-8') as file:
        my_file = file.read()
        print(my_file, end="")
