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

    def to_json(self, attrs=None):
        """
        dictionnaire json
        """
        if attrs is None:
            return self.__dict__
        return {key: value for key, value in self.__dict__.items()
                if key in attrs}

    def reload_from_json(self, json):
        """
        Remplace les attributs de l'instance
        """
        for key, value in json.items():
            setattr(self, key, value)
