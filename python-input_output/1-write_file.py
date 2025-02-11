#!/usr/bin/python3
"""
Module doc
"""


def write_file(filename="", text=""):
    """
    Function doc
    """
    with open(filename, 'w', encoding='UTF8') as file:
        file.write(text)
    return len(text)
