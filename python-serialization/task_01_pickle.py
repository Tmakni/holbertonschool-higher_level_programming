#!/usr/bin/python3
import csv
import json
import pickle
"""
Function
"""


class CustomObject

    delf __init__(self, name, age, student)
    self.name = name
    self.age = age
    self.is_student = is_student
    
    def serialize(self, filename)
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current object instance and save it to a file."""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"An error occurred while serializing: {e}")

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from the file."""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print(f"An error occurred while deserializing: {e}")
            return None
