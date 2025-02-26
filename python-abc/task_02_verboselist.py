#!/usr/bin/env python3
from abc import ABC, abstractmethod


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(item)

    def extend(self, iterable):
        super().extend(iterable)
        print(iterable)

    def remove(self, item):
        super().remove(item)
        print(item)

    def pop(self, index=-1):
        item = super().pop(index)
        print(item)
        return item
