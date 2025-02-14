#!/usr/bin/python3
"""
Function
"""


def serialize_and_save_to_file(data, filename):
     with open(filename, 'w') as file:
        json.dump(data, file)
    pass

def load_and_deserialize(filename):
    with open(filename, 'r') as file:
        return json.load(file)
