#!/usr/bin/python3
"""json import"""


import json


def save_to_json_file(my_obj, filename):
    """
    wirte file and return json.dump
    """
    with open(filename, "w", encoding="utf-8")as file:
        json.dump(my_obj, file)
