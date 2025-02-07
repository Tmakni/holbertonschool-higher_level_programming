#!/usr/bin/python3

"""
Module documentation
"""


class CountedIterator:
    """
    Class documentation
    """
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
            item = next(self.iterator)
            self.counter += 1
            return item

    def __iter__(self):
        return self

