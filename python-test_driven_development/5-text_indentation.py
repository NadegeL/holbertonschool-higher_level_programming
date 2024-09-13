#!/usr/bin/python3
"""function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] in ['.', '?', ':']:
            print(text[i])
            print()
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        else:
            print(text[i], end="")
        i += 1
    print()
