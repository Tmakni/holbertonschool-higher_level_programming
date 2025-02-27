#!/usr/bin/python3
"""
Fonction
"""


def write_file(filename="", text=""):
    """
    write a text file and return its content to stdout
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
