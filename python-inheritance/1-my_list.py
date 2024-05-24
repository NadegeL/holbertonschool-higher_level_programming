#!/usr/bin/python3
"""Write a class  with inheritance List"""


class MyList(list):
    """list is sorted in ascending sort"""

    def print_sorted(self):
        print(sorted(self))
