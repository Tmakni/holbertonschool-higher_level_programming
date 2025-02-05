#!/usr/bin/python3
"""Ceci est une description"""


class BaseGeometry:
    """Ceci est une description"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if isinstance(value, int) == 0:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
