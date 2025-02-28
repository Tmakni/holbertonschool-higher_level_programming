#!/usr/bin/python3
"""
Fonction
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Class Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        dictionnaire json
        """
        return self.__dict__
