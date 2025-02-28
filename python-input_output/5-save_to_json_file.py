#!/usr/bin/python3
"""
Fonction
"""
import json
""" import json"""


def save_to_json_file(my_obj, filename):
    """
    Ecris directement dans le fichier.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return json.dump(my_obj, file)
