#!/usr/bin/python3
"""
Fonction
"""


def append_write(filename="", text=""):
    """
    write a text file and return its content to stdout
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
