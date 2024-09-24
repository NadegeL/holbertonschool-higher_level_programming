#!/usr/bin/env python3
"""Create a class named VerboseList that extends the Python list class."""


class VerboseList(list):
    """VorboseList class that inherits from list class"""

    def append(self, item):
        """method redefinition of append"""
        print("Append: {}".format(item))
        # call the original method of the list class using the super() function
        super().append(item)

    def extend(self, item):
        """method redefinition of extend"""
        print("Extend: {}".format(item))
        super().extend(item)

    def remove(self, item):
        """method redefinition of remove"""
        print("Remove: {}".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """method redefinition of pop, don't forget to define index -1"""
        item = super().pop(index)
        print("Pop: {}".format(item))
        return item
