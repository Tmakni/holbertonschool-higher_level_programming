#!/usr/bin/python3
"""write file"""


def write_file(filename="", text=""):
    """
    write a text file
    """
    with open(filename, "w", encoding="utf-8")as file:
        strw = file.write(text)
        return (strw)
