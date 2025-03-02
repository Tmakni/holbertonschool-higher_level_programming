#!/usr/bin/python3
"""
Fonction
"""
import json
"""
import json
"""


def serialize_and_save_to_file(data, filename):
    """
    serialize save file
    """
    with open(filename "w") as file:
        json.dump(data, file)
        pass


def load_and_deserialize(filename):
    """
    load serialize
    """
    with open(filename, "r") as file:
        return json.load(file)
