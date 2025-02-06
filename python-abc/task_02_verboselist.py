#!/usr/bin/python3

"""
Module task_02_verboselist.py
Provides VerboseList class
"""

from abc import ABC, abstractmethod


class VerboseList(list):
    """
    VerboseList class
    """
    pass


def __init__(self, *args):
    """
    Initialize the class
    """
    super().__init__(*args)


def append(self, item):
    """
    append method
    """
    print(f"Added {item} to the list.")
    super().append(item)


def extend(self, items):
    """
    extend method
    """
    print(f"Extended the list with {len(items)} items")
    super().extend(item)


def remove(self, item):
    """
    remove method
    """
    print(f"Removed {item} from the list.")
    super().remove(item)


def pop(self, index=-1):
    """
    pop method
    """
    item = super().pop(index)
    print(f"Popped {item} from the list.")
    return item
