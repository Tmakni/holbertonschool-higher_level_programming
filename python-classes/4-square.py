#!/usr/bin/python3
"""
Module 4-square.py
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
        """ Initialize the square """
        self.size = size

    @property
    def size(self):
        """ Getter of the size of the square """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Set the value of the size only if it is a positive integer """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Return the area of the square """
        return self.__size ** 2
