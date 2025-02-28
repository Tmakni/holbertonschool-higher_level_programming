#!/usr/bin/python3
"""
Fonction
"""
import json
""" import json"""


def load_from_json_file(filename):
    """
    Lis le fichier et le converti en python
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.loads(file.read())
