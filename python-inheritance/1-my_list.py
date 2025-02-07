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
        if isinstance(self, int) == 1:
            raise TypeError("Ceci doit etre un entier ...")
        else:
            print(sorted(self))
