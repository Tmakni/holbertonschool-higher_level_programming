#!/usr/bin/python3
"""
Module 1-rectangle
Provides an empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """
        Provides an empty class Rectangle that defines a rectangle
    """
    pass

    def __init__(self, width=0, height=0):
        """ Initialize the rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter of the width of the rectangle """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Set the value of the width of the rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter of the height of the rectangle """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Set the value of the height of the rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
