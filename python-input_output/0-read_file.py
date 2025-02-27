#!/usr/bin/python3
"""
Fonction
"""


def read_file(filename=""):
    """
    Reads a text file and prints its content to stdout
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
