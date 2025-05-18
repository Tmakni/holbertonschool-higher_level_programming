#!/usr/bin/python3
"""
This module defines a function say_my_name.
It prints: My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a name with the format: My name is <first name> <last name>
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
