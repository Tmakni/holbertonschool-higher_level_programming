#!/usr/bin/python3
"""
fonction
"""
import json
"""
fonction
"""


def load_from_json_file(filename):
    """
    Function
    """
    with open(filename, 'r', encoding='utf8') as file:
        text = file.read()
    return json.loads(text)
