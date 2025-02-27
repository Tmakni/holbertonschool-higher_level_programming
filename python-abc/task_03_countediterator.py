#!/usr/bin/env python3
from abc import ABC, abstractmethod


class CountedIterator:
    def __init__(self, some_iterator):
        self.iterator = iter(some_iterator)
        self.count = 0

    def __next__(self):
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        return self.count
