#!/usr/bin/env python3
"""Create a class named CountedIterator
that extends the built-in iterator class."""


class CountedIterator:
    """class CountedIterator"""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """method __iter__"""
        return self

    def __next__(self):
        """method __next__"""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """method get_count"""
        return self.count
