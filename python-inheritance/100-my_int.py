#!/usr/bin/python3
"""Write a class MyInt that inherits from int"""


class MyInt(int):
    """MyInt class"""

    def __eq__(self, other):
        """inverse == en != operators"""
        return super().__ne__(other)

    def __ne__(self, other):
        """inverse != en == operators"""
        return super().__eq__(other)
