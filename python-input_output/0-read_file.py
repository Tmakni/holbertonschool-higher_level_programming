#!/usr/bin/python3
"""
module doc
"""


def read_file(filename=""):
    """
    function doc
    """
    with open(filename, encoding='UTF8') as file:
        text = file.read()
        print(text, end="")
