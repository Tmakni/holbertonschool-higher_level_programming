#!/usr/bin/python3
"""json import"""


import json


def load_from_json_file(filename):
    """
    wirte file et lit depuis le fichier ouvert(json.load)
    """
    with open(filename, "r", encoding="utf-8")as file:
        return json.load(file)
