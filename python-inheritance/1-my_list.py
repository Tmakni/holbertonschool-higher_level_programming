#!/usr/bin/python3
"""
Module 1-my_list.py
Provides a class MyList that inherits from list
"""


class MyList(list):
    """
    Provides a class MyList that inherits from list
    """
    def print_sorted(self):
        """
        Print a sorted list of int
        """
        print(sorted(self))
