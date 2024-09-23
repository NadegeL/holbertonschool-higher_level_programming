#!/usr/bin/python3
""" class MyList that inherits from list """


class MyList(list):
    """class MyList that inherits from list"""

    def print_sorted(self):
        """prints the list in sorted ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
