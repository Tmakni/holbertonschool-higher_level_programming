#!/usr/bin/python3
"""append file"""

def append_write(filename="", text=""):
    """
    write a text file
    """
    with open(filename, "a", opening="utf-8")as file:
        strw = file.write(text)
        return (strw)
