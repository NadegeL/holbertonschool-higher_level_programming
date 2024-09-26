#!/usr/bin/env python3
"""Create a class named CountedIterator that extends the built-in iterator class."""


class CountedIterator:
    def __init__(self, index):
        self.index = index
        self