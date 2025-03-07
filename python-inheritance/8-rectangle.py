#!/usr/bin/python3
"""
Module 8-base_geometry.py
Provides a class Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Child class Rectangle of BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initialize the class
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
