#!/usr/bin/python3
"""
Module 3-square.py
Provides an empty class Square that defines a square
"""


class Square:
    """
    Provides an empty class Square that defines a square

    Attribute :
        Size (private) of the square

    Returns :
        Current square area
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
