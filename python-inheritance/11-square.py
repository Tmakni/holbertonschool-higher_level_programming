#!/usr/bin/python3
"""
This module is used to implement the Square class
"""
Rectangle = __import__('9-rectangle').Rectangle
"""
We import the parent class
"""


class Square(Rectangle):
    """
    Class for Squares, inheriting of rectangles
    """
    def __init__(self, size):
        """
        initializes an instance of the class
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        return area of instance
        """
        return self.__size**2

    def __str__(self):
        """
        str representation
        """
        return (f"[Square] {self.__size}/{self.__size}")