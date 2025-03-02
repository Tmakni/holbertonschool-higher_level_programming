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
        json.dump(data)
    pass

def load_and_deserialize(filename):
        """
        load serialize
        """
    return json.load(filename)
