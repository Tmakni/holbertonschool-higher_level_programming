#!/usr/bin/python3
"""
module doc
"""


def append_write(filename="", text=""):
    """
    Function
    """
    with open(filename, 'a', encoding='UTF8') as file:
        file.write(text)
        return len(text)
