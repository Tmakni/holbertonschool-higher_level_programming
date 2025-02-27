#!/usr/bin/python3
    """
    Fonction
    """

def read_file(filename="")
    """
    Reads a text file and prints its content to stdout

    param filename: The path to the file (defaults to an empty string)
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
