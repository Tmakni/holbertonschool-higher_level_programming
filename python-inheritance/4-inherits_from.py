#!/usr/bin/python3
"""
Module 4-inherits_from.py
Provides a function inherits_from
"""


def inherits_from(obj, a_class):
    """
    Verify if the object is an instance of a class inherited from a other class
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
